import os
import psycopg2
from contextlib import contextmanager

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')


@contextmanager
def get_db_cursor():
    connection = psycopg2.connect(DATABASE_URL)
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def select_by_query(query):
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM contacts WHERE to_tsvector('english', first_name || ' ' || last_name) @@ to_tsquery('english', %s)",
            (query,))
        results = cursor.fetchall()

    return results
