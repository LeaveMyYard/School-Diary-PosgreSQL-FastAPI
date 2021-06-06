from typing import Any, TypeVar, Generic
from pydantic import BaseModel
from typing import Optional
import pg8000
import abc
import uuid

_Schema = TypeVar("_Schema", bound=BaseModel)


class BaseCRUD(abc.ABC, Generic[_Schema]):
    __tablename__: str
    __id_name__: str

    @property
    def _tablename(self) -> str:
        if not hasattr(self, "__tablename__"):
            raise ValueError("No __tablename__ static attribute is set")
        return self.__tablename__

    @property
    def _id_name(self) -> str:
        if not hasattr(self, "__id_name__"):
            raise ValueError("No __id_name__ static attribute is set")
        return self.__id_name__

    @staticmethod
    @abc.abstractmethod
    def list_to_schema(args: list[Any]) -> _Schema:
        ...

    def get(self, db: pg8000.Connection, *, id: uuid.UUID) -> Optional[_Schema]:
        data = db.run(
            "SELECT * FROM :table WHERE :id_name = :id",
            table=self._tablename,
            id_name=self._id_name,
            id=id,
        )
        if data == []:
            return None
        return self.list_to_schema(data[0])

    @abc.abstractmethod
    def create(self, db: pg8000.Connection, *, obj: _Schema) -> None:
        ...

    @abc.abstractmethod
    def update(self, db: pg8000.Connection, *, id: uuid.UUID, obj: _Schema) -> None:
        ...

    def delete(self, db: pg8000.Connection, *, id: uuid.UUID) -> None:
        db.run(
            "DELETE FROM :table WHERE :id_name = :id",
            table=self._tablename,
            id_name=self._id_name,
            id=id,
        )