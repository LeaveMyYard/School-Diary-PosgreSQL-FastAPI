from app import schemas


def verify_auth(data: schemas.AuthForm) -> bool:
    return True