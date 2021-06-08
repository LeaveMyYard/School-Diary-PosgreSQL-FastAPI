from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import ParentToStudentModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class ParentToStudentCRUD:
    __tablename__ = "ParentToStudent"

    @classmethod
    def list_to_schema(cls, args: list[Any]) -> ParentToStudentModel:
        keys = ParentToStudentModel.__fields__
        return ParentToStudentModel(**dict(zip(keys, args)))

    def get_multi(self, db: pg8000.Connection) -> list[ParentToStudentModel]:
        data = db.run("SELECT * FROM ParentToStudent")
        return [self.list_to_schema(row) for row in data]
