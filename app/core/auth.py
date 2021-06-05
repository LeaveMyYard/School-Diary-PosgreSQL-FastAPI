from app import schemas, db


def verify_auth(data: schemas.AuthForm) -> bool:
    db.connect(data.login, data.password)
    return True