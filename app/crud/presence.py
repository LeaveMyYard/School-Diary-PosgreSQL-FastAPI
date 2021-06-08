from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
import pg8000
import abc
import uuid
from .base import BaseCRUD


class PresenceCRUD:
    __tablename__ = "Presence"

    def get_multi(self, db: pg8000.Connection) -> list[tuple[uuid.UUID, uuid.UUID]]:
        return db.run("SELECT * FROM Presence")

    def get_by_student_and_lesson(
        self, db: pg8000.Connection, student_id: uuid.UUID, lesson_id: uuid.UUID
    ) -> bool:
        data = db.run(
            "SELECT * FROM Presence "
            f"WHERE studentID = '{student_id}' "
            f"AND lessonID = '{lesson_id}'"
        )
        return data != []
