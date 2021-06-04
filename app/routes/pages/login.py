from typing import Any
import base64
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import Form
from fastapi.responses import RedirectResponse
from .base import BasePageCBV
from app import schemas
from app.core import auth

router = InferringRouter()


@cbv(router)
class LoginPageCBV(BasePageCBV):
    @router.get("/")
    def get_login_page(self) -> Any:
        return self._create_template("login.jinja")

    @router.post("/")
    def authenticate(self, login: str = Form(...), password: str = Form(...)) -> Any:
        if not auth.verify_auth(schemas.AuthForm(login=login, password=password)):
            return self._create_template("login.jinja", error="Login failed")

        response = RedirectResponse(url="/", status_code=302)
        response.set_cookie("auth", value=f"{login}:{password}")
        return response
