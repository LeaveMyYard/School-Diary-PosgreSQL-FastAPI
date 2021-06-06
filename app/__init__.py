from app.schemas.teacher import TeacherModel
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app import routes, db, crud
from datetime import date

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(routes.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    status_code = 422
    if "cookie -> auth" in str(exc):
        return RedirectResponse("/login")

    return Jinja2Templates(directory="templates").TemplateResponse(
        "error.jinja",
        {"request": request, "error": exc, "status_code": status_code},
        status_code=status_code,
    )


@app.on_event("startup")
def on_startup() -> None:
    connection = db.connect("postgres", "qweR1tyFUn123")
    db.init_database(connection)
    db.add_default_data(connection)
