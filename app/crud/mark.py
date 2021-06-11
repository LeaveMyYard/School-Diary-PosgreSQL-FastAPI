from typing import Any, TypeVar, Generic
from app.schemas import MarkModel
import pg8000
import abc
import collections
import uuid
from .base import BaseCRUD


class MarkCRUD(BaseCRUD[MarkModel]):
    __tablename__ = "Mark"
    __id_name__ = "markID"

    def update(self, db: pg8000.Connection, *, id: uuid.UUID, obj: MarkModel) -> None:
        ...

    def get_marks_by_lesson(
        self, db: pg8000.Connection, *, lesson_id: uuid.UUID
    ) -> list[MarkModel]:
        data = db.run(
            "SELECT * FROM Mark WHERE lessonID = :lesson_id", lesson_id=lesson_id
        )
        return [self.list_to_schema(row) for row in data]

    def get_student_marks_by_lesson(
        self, db: pg8000.Connection, *, lesson_id: uuid.UUID
    ) -> dict[uuid.UUID, list[MarkModel]]:
        marks = self.get_marks_by_lesson(db, lesson_id=lesson_id)
        result: dict[uuid.UUID, list[MarkModel]] = collections.defaultdict(list)
        for mark in marks:
            result[mark.student_id].append(mark)
        return result
