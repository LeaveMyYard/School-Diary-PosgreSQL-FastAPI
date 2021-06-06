from typing import Any, TypeVar, Generic
from app.schemas import TeacherModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class TeacherCRUD(BaseCRUD[TeacherModel]):
    __tablename__ = "Teacher"
    __id_name__ = "teacherID"

    @staticmethod
    def list_to_schema(args: list[Any]) -> TeacherModel:
        keys = (
            "teacher_id",
            "full_name",
            "address",
            "phone_number",
            "sex",
            "date_of_birth",
            "status",
            "email",
            "additional_info",
        )
        return TeacherModel(**dict(zip(keys, args)))

    def create(self, db: pg8000.Connection, *, obj: TeacherModel) -> None:
        db.run(
            f"INSERT INTO {self._tablename} VALUES "
            f"('{obj.teacher_id}', '{obj.full_name}', '{obj.address}', "
            f"'{obj.phone_number}', '{obj.sex}', '{obj.date_of_birth}', "
            f"'{obj.status}', '{obj.email}', '{obj.additional_info}')",
        )

    def update(
        self, db: pg8000.Connection, *, id: uuid.UUID, obj: TeacherModel
    ) -> None:
        ...