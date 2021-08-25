from fastapi import Cookie, HTTPException, Depends
from typing import Optional
from app import db, schemas
import pg8000


def get_current_user(
    auth: Optional[str] = Cookie(...),
) -> tuple[schemas.Role, str, str]:
    if auth is None:
        raise HTTPException(401, detail="Not authorized")

    role, login, password = auth.split(":")
    return role, login, password


def get_db(
    auth: tuple[schemas.Role, str, str] = Depends(get_current_user)
) -> pg8000.Connection:
    role, _, _ = auth
    if role == "administrator":
        return db.connect(db.constants.ADMIN_USER, db.constants.PASSWORD)
    if role == "teacher":
        return db.connect(db.constants.TEACHER_USER, db.constants.PASSWORD)
    if role == "student":
        return db.connect(db.constants.STUDENT_USER, db.constants.PASSWORD)
    if role == "parent":
        return db.connect(db.constants.PARENT_USER, db.constants.PASSWORD)

    raise NotImplementedError(role)
