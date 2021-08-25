from pydantic import BaseModel, Field
from datetime import date
import uuid
from typing import Optional


class TeacherModel(BaseModel):
    teacher_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    full_name: str
    address: str
    phone_number: str
    sex: str
    date_of_birth: date
    status: str
    email: str
    login: str
    password: str
    additional_info: str = ""

    @property
    def age(self) -> int:
        return (date.today() - self.date_of_birth).days // 365
