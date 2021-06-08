from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid


class StudentModel(BaseModel):
    student_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    full_name: str
    class_id: uuid.UUID
    address: str
    phone_number: str
    sex: str
    date_of_birth: date
    status: str
    email: str

    @property
    def age(self) -> int:
        return (date.today() - self.date_of_birth).days // 365