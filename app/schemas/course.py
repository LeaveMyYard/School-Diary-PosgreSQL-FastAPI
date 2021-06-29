from pydantic import BaseModel, Field
from datetime import date
import uuid


class CourseModel(BaseModel):
    course_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    teacher_id: uuid.UUID
    course_name: str
    old: bool = False
