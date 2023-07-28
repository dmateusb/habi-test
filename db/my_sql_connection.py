import mysql.connector
import os

class MySQLConnection:
    def __call__(self, func) -> None:
        def wrapper(*args, **kwargs):
            connector =  mysql.connector.connect(
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                host=os.getenv("HOST"),
                database=os.getenv("DATABASE"),
                port=os.getenv("PORT")
            )

            try:
                result = func(*args, **kwargs, connection=connector)
                connector.commit()
                return result
            except Exception as e:
                connector.rollback()
                raise e
            finally:
                connector.close()
        return wrapper