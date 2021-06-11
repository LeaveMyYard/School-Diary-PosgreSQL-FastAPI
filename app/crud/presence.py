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
        self, db: pg8000.Connection, *, student_id: uuid.UUID, lesson_id: uuid.UUID
    ) -> bool:
        data = db.run(
            "SELECT * FROM Presence "
            f"WHERE studentID = '{student_id}' "
            f"AND lessonID = '{lesson_id}'"
        )
        return data != []

    def get_present_on_lesson(
        self, db: pg8000.Connection, lesson_id: uuid.UUID
    ) -> set[uuid.UUID]:
        data = db.run(
            "SELECT studentID from Presence WHERE lessonID = :lesson_id",
            lesson_id=lesson_id,
        )
        return {row[0] for row in data}
