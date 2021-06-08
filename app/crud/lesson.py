from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import LessonModel
import pg8000
import abc
from datetime import date
import uuid
from .base import BaseCRUD


class LessonCRUD(BaseCRUD[LessonModel]):
    __tablename__ = "Lesson"
    __id_name__ = "lessonID"

    def update(self, db: pg8000.Connection, *, id: uuid.UUID, obj: LessonModel) -> None:
        ...

    def get_multi_by_date_and_class(
        self, db: pg8000.Connection, *, class_id: uuid.UUID, day: date
    ) -> list[LessonModel]:
        data = db.run(
            "SELECT * FROM Lesson "
            f"WHERE Lesson.classID = '{class_id}' "
            f"AND Lesson.date = '{day}' "
            "ORDER BY lessonNumber ASC"
        )
        return [self.list_to_schema(row) for row in data]
