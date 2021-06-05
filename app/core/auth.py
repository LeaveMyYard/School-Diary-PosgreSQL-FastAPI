from app import schemas, db


def verify_auth(data: schemas.AuthForm) -> bool:
    try:
        db.connect(data.login, data.password)
    except:
        return False
    return True