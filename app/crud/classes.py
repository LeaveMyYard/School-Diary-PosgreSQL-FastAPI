from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import TeacherModel
from datetime import date
import pg8000
import abc
import uuid
from .base import BaseCRUD


class ClassCRUD(BaseCRUD[ClassModel]):
    __tablename__ = "Classes"
    __id_name__ = "classID"

    def update(self, db: pg8000.Connection, *, id: uuid.UUID, obj: ClassModel) -> None:
        ...

    def get_multi_by_course(
        self, db: pg8000.Connection, *, course_id: uuid.UUID, year: int
    ) -> list[ClassModel]:
        data = db.run(
            "SELECT * FROM Classes "
            "INNER JOIN YearCourses "
            "ON YearCourses.classID = Classes.classID "
            "INNER JOIN Course "
            "ON Course.courseID = YearCourses.courseID "
            f"WHERE Course.courseID = '{course_id}'"
        )
        return [self.list_to_schema(row) for row in data]

    def get_last_lesson_day(self, db: pg8000.Connection, *, id: uuid.UUID) -> date:
        data = db.run(
            "SELECT MAX(date) " "FROM Lesson " "WHERE Lesson.classID = :id", id=id
        )
        if data[0][0] is None:
            return date.today()
        return min(data[0][0], date.today())
