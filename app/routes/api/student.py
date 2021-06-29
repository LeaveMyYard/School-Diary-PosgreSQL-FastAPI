from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException
from ..base import BaseAuthCBV
from typing import Any
from app import schemas, crud
import pg8000

router = InferringRouter()


@cbv(router)
class StudentCBV(BaseAuthCBV):
    @router.post("/")
    def create_new_student(self, data: schemas.StudentModel) -> schemas.StudentModel:
        try:
            crud.student.create(self.db, obj=data)
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail=str(error)) from error
        return data
