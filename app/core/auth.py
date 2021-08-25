from app import schemas, db, crud
from typing import Union


def verify_auth(data: schemas.AuthForm) -> bool:
    try:
        connection = db.connect(db.constants.SUPER_ADMIN_USER, db.constants.PASSWORD)
        if data.role == "administrator":
            return (
                data.login == db.constants.ADMIN_USER
                and data.password == db.constants.PASSWORD
            )

        result: Union[
            schemas.StudentModel, schemas.TeacherModel, schemas.ParentModel, None
        ]
        result = getattr(crud, data.role).get_by_login(connection, login=data.login)

        if result is None:
            return False

        return result.password == data.password
    except Exception:
        return False
