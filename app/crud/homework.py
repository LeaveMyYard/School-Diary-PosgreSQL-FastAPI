from typing import Any, Optional, TypeVar, Generic
from app.schemas import HomeworkModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class HomeworkCRUD(BaseCRUD[HomeworkModel]):
    __tablename__ = "Homework"
    __id_name__ = "homeworkID"

    def update(
        self, db: pg8000.Connection, *, id: uuid.UUID, obj: HomeworkModel
    ) -> None:
        ...

    def get_by_lesson(
        self, db: pg8000.Connection, *, lesson_id: uuid.UUID
    ) -> Optional[HomeworkModel]:
        data = db.run(
            f"SELECT * FROM {self._tablename} WHERE lessonID = :lesson_id",
            lesson_id=lesson_id,
        )
        if data == []:
            return None
        return self.list_to_schema(data[0])
