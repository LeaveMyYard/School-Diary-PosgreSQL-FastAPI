from typing import Any
import pg8000.native
import pg8000
import os
import csv
from app import crud


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


def add_default_data(connection: pg8000.Connection) -> None:
    data_dir = "app/db/data"
    data_tables = os.listdir(data_dir)
    for data_table in sorted(data_tables):
        table_name = data_table.split("_")[1].split(".")[0]
        file_loc = os.path.join(data_dir, data_table)
        if not hasattr(crud, table_name.lower()):
            raise NotImplementedError(table_name)

        crud_obj: crud.BaseCRUD = getattr(crud, table_name.lower())
        if crud_obj.get_multi(connection) == []:
            with open(file_loc, "rb") as file:
                connection.run(
                    f"COPY {table_name} FROM STDIN WITH (FORMAT CSV)", stream=file
                )
