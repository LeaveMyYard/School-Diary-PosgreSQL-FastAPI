from fastapi.templating import Jinja2Templates
from abc import ABC
from typing import Any, TypedDict
from fastapi import Request, Depends
from ..base import BaseDatabaseCBV
from .. import deps
from app import schemas


class BasePageCBV(ABC):
    templates = Jinja2Templates(directory="templates")
    request: Request

    def _create_template(
        self, template: str, nav: schemas.NavData = schemas.NavData(), **kwargs: Any
    ) -> Any:
        return self.templates.TemplateResponse(
            template, kwargs | self._get_additional_args() | {"nav": nav}
        )

    def _get_additional_args(self) -> dict[str, Any]:
        return {"request": self.request}


class BasePageWithAuthCBV(BasePageCBV, BaseDatabaseCBV):
    auth: tuple[str, str] = Depends(deps.get_current_user)

    @property
    def username(self) -> str:
        return self.auth[0]

    def _get_additional_args(self) -> dict[str, Any]:
        return super()._get_additional_args() | {
            "username": self.username,
            "panel_type": "Administrator",
        }
