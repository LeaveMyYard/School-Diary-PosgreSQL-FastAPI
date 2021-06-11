from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timedelta
from app import core


class ClassModel(BaseModel):
    class_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    teacher_id: uuid.UUID
    year_started: int
    name: str

    @property
    def grade(self) -> int:
        return core.calc_grade(self.year_started)

    @property
    def display_name(self) -> str:
        return core.format_display_name(self.grade, self.name, self.year_started)
