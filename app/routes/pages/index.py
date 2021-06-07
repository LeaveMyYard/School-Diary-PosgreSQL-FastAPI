from typing import Any, Optional
import base64
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Depends
from fastapi.responses import RedirectResponse
from .base import BasePageWithAuthCBV
from app import schemas
from app.routes import deps

router = InferringRouter()


@cbv(router)
class IndexPageCBV(BasePageWithAuthCBV):
    @router.get("/")
    def get_index_page(self) -> Any:
        return self._create_template(
            "index.jinja", username=self.username, panel_type="Student"
        )
