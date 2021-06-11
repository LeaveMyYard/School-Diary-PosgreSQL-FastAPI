from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from app import core
import uuid


class LessonModel(BaseModel):
    lesson_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    course_id: uuid.UUID
    class_id: uuid.UUID
    lesson_number: int
    date: date
    audience: Optional[int]


class StudentLessonModel(LessonModel):
    homework: Optional[str]
    present: bool = True
    marks: list[int] = []
    course_name: str

    @property
    def marks_data(self) -> str:
        return ",".join(str(mark) for mark in self.marks)


class TeacherLessonModel(LessonModel):
    course_name: str
    class_name: str
    class_year_started: int

    @property
    def class_display_name(self) -> str:
        return core.format_display_name(
            core.calc_grade(self.class_year_started),
            self.class_name,
            self.class_year_started,
        )
