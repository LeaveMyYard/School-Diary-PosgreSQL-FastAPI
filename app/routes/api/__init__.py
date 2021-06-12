from fastapi_utils.inferring_router import InferringRouter
from . import user

router = InferringRouter()
router.include_router(user.router, prefix="/user")