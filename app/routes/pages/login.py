from typing import Any
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base import BasePageCBV

router = InferringRouter()


@cbv(router)
class LoginPageCBV(BasePageCBV):
    @router.get("/")
    def get_login_page(self) -> Any:
        return self._create_template("login.jinja")
