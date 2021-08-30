from fastapi import Cookie, HTTPException, Depends
from typing import Iterator, Optional
from app import db, schemas
from app.core import auth as auth_module
import pg8000


def get_current_user(
    auth: Optional[str] = Cookie(...),
) -> tuple[schemas.Role, str, str]:
    if auth is None:
        raise HTTPException(401, detail="Not authorized")

    role, login, password = auth.split(":")
    if not auth_module.verify_auth(
        schemas.AuthForm(role=role, login=login, password=password)
    ):
        raise HTTPException(400, "Invalid login data")
    return role, login, password


def get_db(
    auth: tuple[schemas.Role, str, str] = Depends(get_current_user)
) -> Iterator[pg8000.Connection]:
    role, _, _ = auth
    if role == "administrator":
        conn = db.connect(db.constants.ADMIN_USER, db.constants.PASSWORD)
    elif role == "teacher":
        conn = db.connect(db.constants.TEACHER_USER, db.constants.PASSWORD)
    elif role == "student":
        conn = db.connect(db.constants.STUDENT_USER, db.constants.PASSWORD)
    elif role == "parent":
        conn = db.connect(db.constants.PARENT_USER, db.constants.PASSWORD)
    else:
        raise NotImplementedError(role)

    try:
        yield conn
    finally:
        conn.close()
