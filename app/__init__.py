from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import routes

app = FastAPI(debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(routes.router)