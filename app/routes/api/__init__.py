from fastapi_utils.inferring_router import InferringRouter
from . import (
    homework,
    lesson,
    year_courses,
    course,
    mark,
    presence,
    teacher,
    student,
)

router = InferringRouter()
router.include_router(homework.router, prefix="/homework")
router.include_router(lesson.router, prefix="/lesson")
router.include_router(year_courses.router, prefix="/yearCourses")
router.include_router(course.router, prefix="/course")
router.include_router(mark.router, prefix="/mark")
router.include_router(presence.router, prefix="/presence")
router.include_router(teacher.router, prefix="/teacher")
router.include_router(student.router, prefix="/student")
