from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import StudentModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class StudentCRUD(BaseCRUD[StudentModel]):
    __tablename__ = "Student"
    __id_name__ = "studentID"

    def update(
        self, db: pg8000.Connection, *, id: uuid.UUID, obj: StudentModel
    ) -> None:
        ...

    def get_multi_by_class(
        self, db: pg8000.Connection, *, class_id: uuid.UUID
    ) -> list[StudentModel]:
        data = db.run(f"SELECT * FROM Student WHERE Student.classID = '{class_id}'")
        return [self.list_to_schema(row) for row in data]
