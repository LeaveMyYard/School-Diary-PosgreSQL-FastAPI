from fastapi_utils.inferring_router import InferringRouter
from fastapi.responses import HTMLResponse

from app.routes import api, pages

router = InferringRouter()
router.include_router(api.router, prefix="/api")
router.include_router(pages.router, default_response_class=HTMLResponse)
