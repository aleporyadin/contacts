# Contacts Project Setup

This project involves interacting with the Nimble API to update and manage contacts, as well as providing a search feature through a Flask web application. The project uses PostgreSQL as the database and Celery for periodic updates.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Components](#components)
  - [api.py](#apipy)
  - [app.py](#apppy)
  - [database.py](#databasepy)
  - [import_csv.py](#import_csvpy)
  - [tasks.py](#taskspy)

- [Setup](#setup)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Prerequisites

Before you start, make sure you have the following requirements installed:

- Python (3.6+)
- PostgreSQL
- Redis (for Celery)
- `virtualenv` (recommended)

## Components

### `api.py`

This module handles interactions with the Nimble API. It fetches contact data and updates the local database. Make sure to set the `NIMBLE_API_KEY` and `API_NIMBLE_URL` environment variables in the `.env` file.

### `app.py`

The Flask web application provides an API endpoint `/search` to search for contacts based on a query string. It communicates with the database to retrieve search results.

### `database.py`

This module manages the PostgreSQL database connection. It includes functions to create a database cursor and retrieve contacts based on a search query.

### `import_csv.py`

This script allows you to import contacts from a CSV file into the database. The CSV file should contain columns for `first_name`, `last_name`, and `email`.

### `tasks.py`

Celery tasks are defined in this module. It includes a task to periodically update contacts from the Nimble API. The schedule for updates is configured in the `beat_schedule` dictionary.


## Setup

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone <repository_url>
    cd contacts
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a PostgreSQL database named `contacts`.

    ```sql
    CREATE DATABASE contacts;
    ```

5. Create the `contacts` table within the database:

    ```sql
    CREATE TABLE contacts (
        id SERIAL PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    );
    ```

6. Configure environment variables:

    Create a `.env` file in the project root and add the following contents,
    *replacing values USER(postgres) and password(Aa11!!az) *:

    ```env
    DATABASE_URL=postgresql://postgres:Aa11!!az@localhost/contacts
    NIMBLE_API_KEY=NxkA2RlXS3NiR8SKwRdDmroA992jgu
    API_NIMBLE_URL=https://api.nimble.com/api/v1/contacts
    CELERY_BROKER_URL=pyamqp://guest@localhost//
    ```

7. Run the Flask application:

    ```bash
    python app.py
    ```

    The application will start and serve at `http://127.0.0.1:5000`.

8. Run Celery for periodic contact updates:

    ```bash
    celery -A tasks beat --loglevel=info
    celery -A tasks worker --loglevel=info
    ```

    Celery will fetch and update contacts every minute (adjust the schedule in `tasks.py` as needed).

## Usage

- Access the web application at `http://127.0.0.1:5000` to search for contacts using the `/search` endpoint. 
For search example name Alex, need use like it: `http://127.0.0.1:5000/search?q=Alex`

- To import contacts from a CSV file(file must be in root folder project), use `import_csv.py`:

    ```bash
    python import_csv.py
    ```

## Credits

This project was created by [Oleksandr Poriadin].

## License

This project is licensed under the [MIT License](LICENSE).

