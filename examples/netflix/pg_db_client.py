import psycopg2
from pgvector.psycopg2 import register_vector

from configuration import get_configuration


class PgDbClient:

    def __init__(self, host, port, user, password, database):
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        register_vector(self.conn)

    def execute(self, query: str, values: tuple):
        with self.conn.cursor() as cursor:
            cursor.execute(query, values)
            self.conn.commit()

    def execute_with_result(self, query: str, values: tuple):
        with self.conn.cursor() as cursor:
            register_vector(cursor)
            cursor.execute(query, values)
            return cursor.fetchall()

    def close(self):
        self.conn.close()

config = get_configuration()

_pg_client = PgDbClient(
    host=config.pg_host,
    port=config.pg_port,
    user=config.pg_user,
    password=config.pg_password,
    database=config.pg_database
)

def get_pg_db_client() -> PgDbClient:
    return _pg_client
