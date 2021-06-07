from typing import Any, TypeVar, Generic
from pydantic import BaseModel
from typing import Optional, get_args
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
            raise AttributeError("No __tablename__ static attribute is set")
        return self.__tablename__

    @property
    def _id_name(self) -> str:
        if not hasattr(self, "__id_name__"):
            raise AttributeError("No __id_name__ static attribute is set")
        return self.__id_name__

    @classmethod
    def list_to_schema(cls, args: list[Any]) -> _Schema:
        schema: type[_Schema] = get_args(cls.__orig_bases__[0])[0]  # type: ignore
        keys = schema.__fields__
        return schema(**dict(zip(keys, args)))

    def get(self, db: pg8000.Connection, *, id: uuid.UUID) -> Optional[_Schema]:
        data = db.run(
            f"SELECT * FROM {self._tablename} WHERE {self._id_name} = :id",
            id=id,
        )
        if data == []:
            return None
        return self.list_to_schema(data[0])

    def get_multi(self, db: pg8000.Connection) -> list[_Schema]:
        data = db.run(f"SELECT * FROM {self._tablename}")
        return [self.list_to_schema(row) for row in data]

    def create(self, db: pg8000.Connection, *, obj: _Schema) -> None:
        db.run(
            f"INSERT INTO {self._tablename} VALUES "
            "(" + ", ".join(f"'{val}'" for val in obj.dict().values()) + ")",
        )

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