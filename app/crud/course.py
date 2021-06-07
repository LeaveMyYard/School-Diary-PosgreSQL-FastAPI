from typing import Any, TypeVar, Generic
from app.schemas import CourseModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class CourseCRUD(BaseCRUD[CourseModel]):
    __tablename__ = "Course"
    __id_name__ = "courseID"

    def update(self, db: pg8000.Connection, *, id: uuid.UUID, obj: CourseModel) -> None:
        ...

    def get_multi_by_teacher(
        self, db: pg8000.Connection, *, teacher_id: uuid.UUID
    ) -> list[CourseModel]:
        data = db.run(
            f"SELECT * FROM {self._tablename} "
            f"WHERE teacherID = '{teacher_id}' "
            "ORDER BY old",
        )
        return [self.list_to_schema(row) for row in data]