from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
import uuid


class LessonModel(BaseModel):
    lesson_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    course_id: uuid.UUID
    class_id: uuid.UUID
    lesson_number: int
    date: date
    audience: Optional[int]