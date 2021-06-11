from typing import Optional
from pydantic import BaseModel, Field
from datetime import date
import uuid


class MarkModel(BaseModel):
    mark_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    lesson_id: uuid.UUID
    student_id: uuid.UUID
    mark_value: int
    type: str
    description: Optional[str]
    homework_id: Optional[uuid.UUID]