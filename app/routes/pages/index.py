from typing import Any, Optional
import base64
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends
from fastapi.responses import RedirectResponse
from .base import BasePageWithAuthCBV
from app import schemas, crud
from app.routes import deps

router = InferringRouter()


@cbv(router)
class IndexPageCBV(BasePageWithAuthCBV):
    @router.get("/")
    def get_index_page(self) -> Any:
        teachers = crud.teacher.get_multi(self.db)
        classes = crud.classes.get_multi(self.db)
        return self._create_template("index.jinja", teachers=teachers, classes=classes)
