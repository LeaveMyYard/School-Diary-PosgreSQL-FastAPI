from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException
from ..base import BaseAuthCBV
from typing import Any
from app import schemas, crud
import pg8000

router = InferringRouter()


@cbv(router)
class MarkCBV(BaseAuthCBV):
    @router.post("/")
    def create_new_mark(self, data: schemas.MarkModel) -> schemas.MarkModel:
        try:
            crud.mark.create(self.db, obj=data)
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail=str(error)) from error
        return data
