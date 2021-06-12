from fastapi.templating import Jinja2Templates
from abc import ABC
from typing import Any, TypedDict
from fastapi import Request, Depends
from ..base import BaseAuthCBV
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


class BasePageWithAuthCBV(BasePageCBV, BaseAuthCBV):
    @property
    def username(self) -> str:
        return self.auth[0]

    def _get_user_role(self, username: str) -> str:
        try:
            return self.db.run(f"""
                WITH RECURSIVE cte AS (
                SELECT oid FROM pg_roles WHERE rolname = '{username}'

                UNION ALL
                SELECT m.roleid
                FROM   cte
                JOIN   pg_auth_members m ON m.member = cte.oid
                )
                SELECT oid::regrole::text AS rolename FROM cte WHERE oid::regrole::text != '{username}'"""
            )[0][0]
        except Exception:
            return "administrator"

    def _get_additional_args(self) -> dict[str, Any]:
        return super()._get_additional_args() | {
            "username": self.username,
            "panel_type": self._get_user_role(self.username).capitalize(),
        }
