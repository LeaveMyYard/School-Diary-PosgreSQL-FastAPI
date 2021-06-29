from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import (
    LessonModel,
    StudentLessonModel,
    TeacherLessonModel,
    ClassLessonModel,
)
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

    def get_multi_by_date_and_student(
        self, db: pg8000.Connection, *, student_id: uuid.UUID, day: date
    ) -> list[StudentLessonModel]:
        with open("app/db/sql/queries/student_day_schedule.sql") as query_file:
            data = db.run(query_file.read(), student_id=student_id, day=day)
            return [self.list_to_schema(row, schema=StudentLessonModel) for row in data]

    def get_multi_by_date_and_class(
        self, db: pg8000.Connection, *, class_id: uuid.UUID, day: date
    ) -> list[ClassLessonModel]:
        with open("app/db/sql/queries/class_day_schedule.sql") as query_file:
            data = db.run(query_file.read(), class_id=class_id, day=day)
            return [self.list_to_schema(row, schema=ClassLessonModel) for row in data]

    def get_multi_by_date_and_teacher(
        self, db: pg8000.Connection, *, teacher_id: uuid.UUID, day: date
    ) -> list[TeacherLessonModel]:
        with open("app/db/sql/queries/teacher_day_schedule.sql") as query_file:
            data = db.run(query_file.read(), teacher_id=teacher_id, day=day)
            return [self.list_to_schema(row, schema=TeacherLessonModel) for row in data]
