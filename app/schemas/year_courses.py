from pydantic import BaseModel, Field
from datetime import date
import uuid


class YearCourseModel(BaseModel):
    year: int
    course_id: uuid.UUID
    class_id: uuid.UUID