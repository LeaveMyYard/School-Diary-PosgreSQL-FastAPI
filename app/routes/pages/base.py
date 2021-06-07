from fastapi.templating import Jinja2Templates
from abc import ABC
from typing import Any
from fastapi import Request, Depends
from ..base import BaseDatabaseCBV
from .. import deps


class BasePageCBV(ABC):
    templates = Jinja2Templates(directory="templates")
    request: Request

    def _create_template(self, template: str, **kwargs: Any) -> Any:
        return self.templates.TemplateResponse(
            template, kwargs | {"request": self.request}
        )


class BasePageWithAuthCBV(BasePageCBV, BaseDatabaseCBV):
    auth: tuple[str, str] = Depends(deps.get_current_user)

    @property
    def username(self) -> str:
        return self.auth[0]
