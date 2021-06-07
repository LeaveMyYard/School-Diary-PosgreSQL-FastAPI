from pydantic import BaseModel, Field
from datetime import date
import uuid


class ParentModel(BaseModel):
    parent_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    full_name: str
    phone_number: str
    sex: str
    date_of_birth: date
    status: str
    email: str