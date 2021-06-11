from typing import Any, Optional
import uuid
from fastapi import HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base import BasePageWithAuthCBV
from app import schemas, crud
from app.core import auth
from datetime import date, timedelta

router = InferringRouter()


@cbv(router)
class TeacherPageCBV(BasePageWithAuthCBV):
    @router.get("/{teacher_id}/")
    def get_login_page(self, teacher_id: uuid.UUID, day: Optional[date] = None) -> Any:
        teacher = crud.teacher.get(self.db, id=teacher_id)
        courses = crud.course.get_multi_by_teacher(self.db, teacher_id=teacher_id)
        if teacher is None:
            raise HTTPException(404, detail="No teacher with such id")
        day = day or crud.teacher.get_last_lesson_day(self.db, id=teacher_id)
        lessons = crud.lesson.get_multi_by_date_and_teacher(
            self.db, teacher_id=teacher_id, day=day
        )
        return self._create_template(
            "teacher.jinja",
            teacher=teacher,
            courses=courses,
            day=day,
            lessons=lessons,
            timedelta=timedelta,
        )
