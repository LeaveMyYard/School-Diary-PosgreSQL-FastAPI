from typing import Any
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
    def get_student_page(self, student_id: uuid.UUID) -> Any:
        student = crud.student.get(self.db, id=student_id)
        if student is None:
            raise HTTPException(404, detail="No student with such id")
        parents = crud.parent.get_multi_by_child(self.db, student_id=student_id)
        class_data = crud.classes.get(self.db, id=student.class_id)
        return self._create_template(
            "student.jinja",
            student=student,
            parents=parents,
            class_data=class_data,
            day=crud.student.get_last_lesson_day(self.db, id=student_id),
        )

    @router.get("/{student_id}/diary/")
    def get_student_diary(self, student_id: uuid.UUID, day: date) -> Any:
        student = crud.student.get(self.db, id=student_id)
        if student is None:
            raise HTTPException(404, detail="No student with such id")
        class_data = crud.classes.get(self.db, id=student.class_id)
        lessons = crud.lesson.get_multi_by_date_and_class(
            self.db, class_id=student.class_id, day=day
        )
        course_data: dict[uuid.UUID, schemas.CourseModel] = {}
        for lesson in lessons:
            if lesson.course_id not in course_data:
                course = crud.course.get(self.db, id=lesson.course_id)
                if course is None:
                    raise RuntimeError(lesson.course_id)
                course_data[lesson.course_id] = course

        presence: dict[uuid.UUID, bool] = {
            lesson.lesson_id: crud.presence.get_by_student_and_lesson(
                self.db, student_id=student_id, lesson_id=lesson.lesson_id
            )
            for lesson in lessons
        }

        return self._create_template(
            "student_diary.jinja",
            student=student,
            class_data=class_data,
            lessons=lessons,
            course_data=course_data,
            presence=presence,
            day=day,
            timedelta=timedelta,
        )
