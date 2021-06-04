from fastapi import Cookie, HTTPException
from typing import Optional


def get_current_user(auth: Optional[str] = Cookie(...)) -> str:
    if auth is None:
        raise HTTPException(401, detail="Not authorized")

    login, password = auth.split(":")
    return login