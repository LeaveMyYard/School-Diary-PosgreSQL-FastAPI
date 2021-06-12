from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException
from ..base import BaseAuthCBV
from typing import Any
from app import schemas
import pg8000

router = InferringRouter()

@cbv(router)
class UserCBV(BaseAuthCBV):
    @router.post("/")
    def create_new_user(self, data: schemas.NewUserData) -> schemas.NewUserData:
        try:
            self.db.run(f"CREATE USER {data.login} WITH PASSWORD '{data.password}'")
            self.db.run(f"GRANT {data.role} TO {data.login}")
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail="User with such login already exists") from error
        return data