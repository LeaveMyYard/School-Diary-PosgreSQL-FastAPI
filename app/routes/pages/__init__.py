from fastapi_utils.inferring_router import InferringRouter
from . import login, index

router = InferringRouter()
router.include_router(login.router, prefix="/login")
router.include_router(index.router)