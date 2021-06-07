from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import YearCourseModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class YearCoursesCRUD:
    __tablename__ = "YearCourses"

    @classmethod
    def list_to_schema(cls, args: list[Any]) -> YearCourseModel:
        keys = YearCourseModel.__fields__
        return YearCourseModel(**dict(zip(keys, args)))

    def get_multi(self, db: pg8000.Connection) -> list[YearCourseModel]:
        data = db.run("SELECT * FROM YearCourses")
        return [self.list_to_schema(row) for row in data]
