from typing import Any, TypeVar, Generic
from app.schemas import TeacherModel
import pg8000
import abc
import uuid
from datetime import date
from .base import BaseCRUD


class TeacherCRUD(BaseCRUD[TeacherModel]):
    __tablename__ = "Teacher"
    __id_name__ = "teacherID"

    def update(
        self, db: pg8000.Connection, *, id: uuid.UUID, obj: TeacherModel
    ) -> None:
        ...

    def get_last_lesson_day(self, db: pg8000.Connection, *, id: uuid.UUID) -> date:
        data = db.run(
            "SELECT MAX(date) "
            "FROM Lesson "
            "INNER JOIN Course "
            "ON Course.courseID = Lesson.courseID "
            "WHERE teacherID = :teacher_id",
            teacher_id=id,
        )
        return min(data[0][0], date.today())