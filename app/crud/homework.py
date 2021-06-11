from typing import Any, TypeVar, Generic
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