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
class ClassPageCBV(BasePageWithAuthCBV):
    @router.get("/{class_id}/")
    def get_class_page(self, class_id: uuid.UUID) -> Any:
        class_data = crud.classes.get(self.db, id=class_id)
        if class_data is None:
            raise HTTPException(404, detail="No class with such id")
        teacher = crud.teacher.get(self.db, id=class_data.teacher_id)
        students = crud.student.get_multi_by_class(self.db, class_id=class_id)
        return self._create_template(
            "classes/single.jinja",
            class_data=class_data,
            teacher=teacher,
            students=students,
        )

    @router.get("/")
    def get_classes_table(self) -> Any:
        classes = crud.classes.get_multi(self.db)
        return self._create_template(
            "classes/table.jinja",
            classes=classes,
            nav=schemas.NavData(classes=True),
        )
