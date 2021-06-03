from fastapi.templating import Jinja2Templates
from abc import ABC
from typing import Any
from fastapi import Request, Depends


class BasePageCBV(ABC):
    templates = Jinja2Templates(directory="templates")
    request: Request

    def _create_template(self, template: str, **kwargs: Any) -> Any:
        return self.templates.TemplateResponse(
            template, kwargs | {"request": self.request}
        )
