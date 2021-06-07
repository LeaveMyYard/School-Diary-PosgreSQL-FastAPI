from fastapi import Cookie, HTTPException, Depends
from typing import Optional
from app import db
import pg8000


def get_current_user(auth: Optional[str] = Cookie(...)) -> tuple[str, str]:
    if auth is None:
        raise HTTPException(401, detail="Not authorized")

    login, password = auth.split(":")
    return login, password


def get_db(auth: tuple[str, str] = Depends(get_current_user)) -> pg8000.Connection:
    return db.connect(*auth)