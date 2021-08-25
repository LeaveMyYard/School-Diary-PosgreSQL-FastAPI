from fastapi.templating import Jinja2Templates
from abc import ABC
from typing import Any
from fastapi import Request, Depends
import pg8000
from app import schemas
from . import deps


class BaseDatabaseCBV:
    db: pg8000.Connection = Depends(deps.get_db)


class BaseAuthCBV(BaseDatabaseCBV):
    auth: tuple[schemas.Role, str, str] = Depends(deps.get_current_user)
