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
class ParentPageCBV(BasePageWithAuthCBV):
    @router.get("/{parent_id}/")
    def get_parent_page(self, parent_id: uuid.UUID) -> Any:
        parent = crud.parent.get(self.db, id=parent_id)
        if parent_id is None:
            raise HTTPException(404, detail="No parent_id with such id")
        students = crud.student.get_multi_by_parent(self.db, parent_id=parent_id)
        return self._create_template("parent.jinja", students=students, parent=parent)
