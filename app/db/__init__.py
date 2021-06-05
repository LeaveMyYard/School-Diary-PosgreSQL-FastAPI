from typing import Any
import pg8000.native
import pg8000
import os


def connect(user: str, password: str) -> pg8000.Connection:
    return pg8000.native.Connection(
        host="postgres", port="5432", password=password, user=user
    )


def init_database(connection: pg8000.Connection) -> None:
    tables_dir = "app/db/sql/tables"
    table_script_names = os.listdir(tables_dir)
    for script in sorted(table_script_names):
        script_full = os.path.join(tables_dir, script)
        with open(script_full) as file:
            sql = file.read()
            if sql != "":
                try:
                    connection.run(sql)
                except pg8000.exceptions.DatabaseError as script_error:
                    raise RuntimeError(script_full) from script_error