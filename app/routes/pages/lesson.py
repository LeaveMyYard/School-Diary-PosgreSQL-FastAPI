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
class LessonPageCBV(BasePageWithAuthCBV):
    @router.get("/{lesson_id}/")
    def get_lesson_page(self, lesson_id: uuid.UUID) -> Any:
        lesson = crud.lesson.get(self.db, id=lesson_id)
        if lesson is None:
            raise HTTPException(404, detail="No lesson with such id")
        course = crud.course.get(self.db, id=lesson.course_id)
        teacher = crud.teacher.get(self.db, id=course.teacher_id)
        class_obj = crud.classes.get(self.db, id=lesson.class_id)
        students = crud.student.get_multi_by_class(self.db, class_id=lesson.class_id)
        marks = crud.mark.get_student_marks_by_lesson(self.db, lesson_id=lesson_id)
        present_students = crud.presence.get_present_on_lesson(
            self.db, lesson_id=lesson_id
        )
        homework = crud.homework.get_by_lesson(self.db, lesson_id=lesson_id)
        return self._create_template(
            "lesson.jinja",
            lesson=lesson,
            course=course,
            teacher=teacher,
            class_obj=class_obj,
            students=students,
            marks=marks,
            present_students=present_students,
            homework=homework,
        )
