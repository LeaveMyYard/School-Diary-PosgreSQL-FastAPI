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
class StudentPageCBV(BasePageWithAuthCBV):
    @router.get("/{student_id}/")
    def get_student_page(
        self, student_id: uuid.UUID, day: Optional[date] = None
    ) -> Any:
        day = day or crud.student.get_last_lesson_day(self.db, id=student_id)
        student = crud.student.get(self.db, id=student_id)
        if student is None:
            raise HTTPException(404, detail="No student with such id")
        parents = crud.parent.get_multi_by_child(self.db, student_id=student_id)
        class_data = crud.classes.get(self.db, id=student.class_id)
        lessons = crud.lesson.get_multi_by_date_and_student(
            self.db, student_id=student_id, day=day
        )
        return self._create_template(
            "student.jinja",
            student=student,
            parents=parents,
            class_data=class_data,
            day=day,
            lessons=lessons,
            timedelta=timedelta,
        )