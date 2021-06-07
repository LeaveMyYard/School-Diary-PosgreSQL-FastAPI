from typing import Any, TypeVar, Generic
from app.schemas import TeacherModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class TeacherCRUD(BaseCRUD[TeacherModel]):
    __tablename__ = "Teacher"
    __id_name__ = "teacherID"

    def update(
        self, db: pg8000.Connection, *, id: uuid.UUID, obj: TeacherModel
    ) -> None:
        ...