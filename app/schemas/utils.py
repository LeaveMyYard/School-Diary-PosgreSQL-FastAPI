from pydantic import BaseModel, Field
from datetime import date, datetime
import uuid


class NavData(BaseModel):
    home: bool = False
    classes: bool = False
    students: bool = False
