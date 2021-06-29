from fastapi_utils.inferring_router import InferringRouter
from . import user, homework, lesson, year_courses, course, mark, presence

router = InferringRouter()
router.include_router(user.router, prefix="/user")
router.include_router(homework.router, prefix="/homework")
router.include_router(lesson.router, prefix="/lesson")
router.include_router(year_courses.router, prefix="/yearCourses")
router.include_router(course.router, prefix="/course")
router.include_router(mark.router, prefix="/mark")
router.include_router(presence.router, prefix="/presence")
