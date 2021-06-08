from fastapi_utils.inferring_router import InferringRouter
from . import login, index, teacher, course, classes, student, parent

router = InferringRouter()
router.include_router(login.router, prefix="/login")
router.include_router(index.router)
router.include_router(teacher.router, prefix="/teacher")
router.include_router(course.router, prefix="/course")
router.include_router(classes.router, prefix="/class")
router.include_router(student.router, prefix="/student")
router.include_router(parent.router, prefix="/parent")