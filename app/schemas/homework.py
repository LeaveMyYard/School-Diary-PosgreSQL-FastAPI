from pydantic import BaseModel, Field
from datetime import date
import uuid


class HomeworkModel(BaseModel):
    homework_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    lesson_id: uuid.UUID
    task: str