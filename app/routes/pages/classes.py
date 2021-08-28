from typing import Any, Optional, cast
import uuid
from fastapi import HTTPException
from fastapi_utils.inferring_router import InferringRouter
from fastapi_utils.cbv import cbv
from .base import BasePageWithAuthCBV
from app import schemas, crud
from app.core import auth
from datetime import datetime, timedelta, date

router = InferringRouter()


@cbv(router)
class ClassPageCBV(BasePageWithAuthCBV):
    @router.get("/{class_id}/")
    def get_class_page(self, class_id: uuid.UUID, *, day: Optional[date] = None) -> Any:
        class_data = crud.classes.get(self.db, id=class_id)
        if class_data is None:
            raise HTTPException(404, detail="No class with such id")

        # Student can only get access to his own class
        if self.role == "student":
            if cast(schemas.StudentModel, self.current_user).class_id != class_id:
                raise HTTPException(
                    403, detail="You can only see information about your own class."
                )

        if self.role == "parent":
            students = crud.student.get_multi_by_parent(
                self.db,
                parent_id=cast(schemas.ParentModel, self.current_user).parent_id,
            )
            if all(student.class_id != class_id for student in students):
                raise HTTPException(
                    403,
                    detail="You can only see information "
                    "about your own children's classes.",
                )

        day = day or crud.classes.get_last_lesson_day(self.db, id=class_id)
        teacher = crud.teacher.get(self.db, id=class_data.teacher_id)
        students = crud.student.get_multi_by_class(self.db, class_id=class_id)
        lessons = crud.lesson.get_multi_by_date_and_class(
            self.db, class_id=class_id, day=day
        )
        study_year = (day - timedelta(days=180)).year
        courses = crud.yearcourses.get_multi_by_course_and_year(
            self.db, class_id=class_id, year=study_year
        )
        all_courses = crud.course.get_multi(self.db)
        return self._create_template(
            "classes/single.jinja",
            class_data=class_data,
            teacher=teacher,
            students=students,
            lessons=lessons,
            day=day,
            timedelta=timedelta,
            courses=courses,
            study_year=study_year,
            year_courses=courses,
            all_courses=all_courses,
        )

    @router.get("/")
    def get_classes_table(self) -> Any:
        classes = crud.classes.get_multi(self.db)
        return self._create_template(
            "classes/table.jinja",
            classes=classes,
            nav=schemas.NavData(classes=True),
        )
