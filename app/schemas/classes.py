from pydantic import BaseModel, Field
import uuid


class ClassModel(BaseModel):
    class_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    teacher_id: uuid.UUID
    year_started: int
    name: str