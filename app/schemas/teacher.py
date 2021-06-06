from pydantic import BaseModel
from datetime import date
import uuid


class TeacherModel(BaseModel):
    teacher_id: uuid.UUID = uuid.uuid4()
    full_name: str
    address: str
    phone_number: str
    sex: str
    date_of_birth: date
    status: str
    email: str
    additional_info: str = ""