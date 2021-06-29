from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from fastapi import HTTPException
from ..base import BaseAuthCBV
from typing import Any
from app import schemas, crud
import pg8000

router = InferringRouter()


@cbv(router)
class YearCoursesCBV(BaseAuthCBV):
    @router.post("/")
    def create_new_year_course(
        self, data: schemas.YearCourseModel
    ) -> schemas.YearCourseModel:
        try:
            crud.yearcourses.create(self.db, obj=data)
        except pg8000.exceptions.DatabaseError as error:
            raise HTTPException(403, detail=str(error)) from error
        return data
