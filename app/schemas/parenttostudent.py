from pydantic import BaseModel
import uuid


class ParentToStudentModel(BaseModel):
    parent_id: uuid.UUID
    student_id: uuid.UUID