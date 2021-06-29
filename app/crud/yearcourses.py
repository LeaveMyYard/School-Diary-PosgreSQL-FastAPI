from app.schemas.course import CourseModel
from app.schemas.classes import ClassModel
from typing import Any, TypeVar, Generic
from app.schemas import YearCourseModel
import pg8000
import abc
import uuid
from .base import BaseCRUD
from .course import CourseCRUD


class YearCoursesCRUD:
    __tablename__ = "YearCourses"

    @classmethod
    def list_to_schema(cls, args: list[Any]) -> YearCourseModel:
        keys = YearCourseModel.__fields__
        return YearCourseModel(**dict(zip(keys, args)))

    def create(self, db: pg8000.Connection, *, obj: YearCourseModel) -> None:
        db.run(
            f"INSERT INTO {self.__tablename__} VALUES (:year, :course_id, :class_id)",
            year=obj.year,
            class_id=obj.class_id,
            course_id=obj.course_id,
        )

    def get_multi(self, db: pg8000.Connection) -> list[YearCourseModel]:
        data = db.run("SELECT * FROM YearCourses")
        return [self.list_to_schema(row) for row in data]

    def get_multi_by_course_and_year(
        self, db: pg8000.Connection, *, class_id: uuid.UUID, year: int
    ) -> list[CourseModel]:
        data = db.run(
            "SELECT * "
            "FROM Course "
            "INNER JOIN YearCourses "
            "ON Course.courseID = YearCourses.courseID "
            "WHERE YearCourses.year = :year "
            "AND YearCourses.classID = :class_id",
            class_id=class_id,
            year=year,
        )
        return [CourseCRUD.list_to_schema(row) for row in data]
