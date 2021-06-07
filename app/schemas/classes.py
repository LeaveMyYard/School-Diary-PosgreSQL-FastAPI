from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timedelta


class ClassModel(BaseModel):
    class_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    teacher_id: uuid.UUID
    year_started: int
    name: str

    @property
    def grade(self) -> int:
        return (datetime.now() - timedelta(days=180)).year - self.year_started + 1
