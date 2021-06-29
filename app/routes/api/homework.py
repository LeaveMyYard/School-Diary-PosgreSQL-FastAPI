from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException
from ..base import BaseAuthCBV
from typing import Any
from app import schemas, crud
import pg8000

router = InferringRouter()


@cbv(router)
class HomeworkCBV(BaseAuthCBV):
    @router.post("/")
    def create_new_homework(self, data: schemas.HomeworkModel) -> schemas.HomeworkModel:
        try:
            crud.homework.create(self.db, obj=data)
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail=str(error)) from error
        return data
