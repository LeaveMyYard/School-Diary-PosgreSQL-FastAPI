from typing import Any
import uuid
from fastapi import HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base import BasePageWithAuthCBV
from app import schemas, crud
from app.core import auth
from datetime import datetime, timedelta

router = InferringRouter()


@cbv(router)
class CoursePageCBV(BasePageWithAuthCBV):
    @router.get("/{course_id}/")
    def get_course_page(self, course_id: uuid.UUID) -> Any:
        course = crud.course.get(self.db, id=course_id)
        if course is None:
            raise HTTPException(404, detail="No teacher with such id")
        teacher = crud.teacher.get(self.db, id=course.teacher_id)
        classes = crud.classes.get_multi_by_course(
            self.db,
            course_id=course_id,
            year=(datetime.now() - timedelta(days=180)).year,
        )
        return self._create_template(
            "course.jinja", course=course, teacher=teacher, classes=classes
        )
