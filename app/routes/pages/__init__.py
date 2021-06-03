from fastapi_utils.inferring_router import InferringRouter
from . import login

router = InferringRouter()
router.include_router(login.router, prefix="/login")