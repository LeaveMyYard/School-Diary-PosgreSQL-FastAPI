from fastapi.templating import Jinja2Templates
from abc import ABC
from typing import Any, Optional, TypedDict, Union
from fastapi import Request, Depends
from ..base import BaseAuthCBV
from .. import deps
from app import schemas, crud
from functools import cache
import uuid


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
        return self.auth[1]

    @property
    def role(self) -> schemas.Role:
        return self.auth[0]

    @property
    @cache
    def current_user(
        self,
    ) -> Union[schemas.StudentModel, schemas.TeacherModel, schemas.ParentModel, None]:
        if self.role == "administrator":
            return None
        return getattr(crud, self.role).get_by_login(self.db, login=self.username)

    @property
    def current_user_id(self) -> Optional[uuid.UUID]:
        if self.role == "administrator":
            return None
        elif self.role == "teacher":
            return self.current_user.teacher_id
        elif self.role == "parent":
            return self.current_user.parent_id
        elif self.role == "student":
            return self.current_user.student_id
        raise NotImplementedError(self.role)

    def _get_additional_args(self) -> dict[str, Any]:
        return super()._get_additional_args() | {
            "username": self.username,
            "panel_type": self.role,
            "current_user_id": self.current_user_id,
        }
