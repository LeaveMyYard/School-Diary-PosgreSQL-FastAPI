from typing import Any
import uuid
from fastapi import HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base import BasePageWithAuthCBV
from app import schemas, crud
from app.core import auth

router = InferringRouter()


@cbv(router)
class TeacherPageCBV(BasePageWithAuthCBV):
    @router.get("/{teacher_id}/")
    def get_login_page(self, teacher_id: uuid.UUID) -> Any:
        teacher = crud.teacher.get(self.db, id=teacher_id)
        if teacher is None:
            raise HTTPException(404, detail="No teacher with such id")
        return self._create_template("teacher.jinja", teacher=teacher)
