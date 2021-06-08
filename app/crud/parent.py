from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import ParentModel
import pg8000
import abc
import uuid
from .base import BaseCRUD


class ParentCRUD(BaseCRUD[ParentModel]):
    __tablename__ = "Parent"
    __id_name__ = "parentID"

    def update(self, db: pg8000.Connection, *, id: uuid.UUID, obj: ParentModel) -> None:
        ...

    def get_multi_by_child(
        self, db: pg8000.Connection, *, student_id: uuid.UUID
    ) -> list[ParentModel]:
        data = db.run(
            "SELECT * FROM Parent "
            "INNER JOIN ParentToStudent "
            "ON Parent.parentID = ParentToStudent.parentID "
            "INNER JOIN Student "
            "ON Student.studentID = ParentToStudent.studentID "
            f"WHERE Student.studentID = '{student_id}'"
        )
        return [self.list_to_schema(row) for row in data]
