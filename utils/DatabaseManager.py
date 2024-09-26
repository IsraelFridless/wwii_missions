import os

from returns.result import Success, Failure, Result
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory


def execute_sql_from_file(sql_file_path: str) -> Result[str, str]:
    if not os.path.exists(sql_file_path):
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

    with session_factory() as session:
        try:
            with open(sql_file_path, 'r') as file:
                sql_script = file.read()

                session.execute(text(sql_script))

            session.commit()
            return Success('SQL file executed successfully!')
        except (SQLAlchemyError, Exception) as e:
            session.rollback()
            return Failure(repr(e))