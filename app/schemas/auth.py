from pydantic import BaseModel


class AuthForm(BaseModel):
    login: str
    password: str