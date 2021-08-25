from pydantic import BaseModel
from typing import Literal

Role = Literal["administrator", "teacher", "student", "parent"]
class AuthForm(BaseModel):
    login: str
    password: str
    role: Role