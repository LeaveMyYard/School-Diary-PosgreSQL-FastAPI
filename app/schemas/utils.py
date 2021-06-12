from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Union, Literal
import uuid


class NavData(BaseModel):
    home: bool = False
    classes: bool = False
    students: bool = False

class NewUserData(BaseModel):
    login: str
    password: str
    role: Union[Literal["Student"], Literal["Teacher"], Literal["Administrator"], Literal["Parent"]]