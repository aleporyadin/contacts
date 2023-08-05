import csv

from database import get_db_cursor
from psycopg2.extras import execute_values


def import_csv_to_db(csv_file):
    with get_db_cursor() as cursor:
        with open(csv_file, 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            data = [(row[0], row[1], row[2]) for row in csv_reader]
            query = "INSERT INTO contacts (first_name, last_name, email) VALUES %s"
            execute_values(cursor, query, data)


if __name__ == "__main__":
    csv_file_path = "contacts.csv"
    import_csv_to_db(csv_file_path)
