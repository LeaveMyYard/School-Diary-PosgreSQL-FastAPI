from typing import Any, TypeVar, Generic, Optional
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
        if data[0][0] is None:
            return date.today()
        return min(data[0][0], date.today())

    def get_by_login(
        self, db: pg8000.Connection, *, login: str
    ) -> Optional[TeacherModel]:
        data = db.run(
            f"SELECT * FROM {self._tablename} WHERE login = :login",
            login=login,
        )
        if data == []:
            return None
        return self.list_to_schema(data[0])
