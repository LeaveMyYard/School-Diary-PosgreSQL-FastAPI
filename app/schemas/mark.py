from pydantic import BaseModel, Field
from datetime import date
import uuid


class MarkModel(BaseModel):
    mark_id: uuid.UUID = Field(default_factory=uuid.uuid4)
