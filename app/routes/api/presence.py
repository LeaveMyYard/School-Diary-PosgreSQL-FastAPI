from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException, Body
from ..base import BaseAuthCBV
from typing import Any
from app import schemas, crud
import pg8000
import uuid

router = InferringRouter()


@cbv(router)
class PresenceCBV(BaseAuthCBV):
    @router.post("/")
    def set_present(
        self, lesson_id: uuid.UUID = Body(...), student_id: uuid.UUID = Body(...)
    ) -> Any:
        try:
            crud.presence.create(self.db, lesson_id=lesson_id, student_id=student_id)
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail=str(error)) from error
        return {}

    @router.delete("/")
    def set_absent(
        self, lesson_id: uuid.UUID = Body(...), student_id: uuid.UUID = Body(...)
    ) -> Any:
        try:
            crud.presence.remove(self.db, lesson_id=lesson_id, student_id=student_id)
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail=str(error)) from error
        return {}
