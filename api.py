import requests
import os
from database import get_db_cursor

NIMBLE_API_KEY = os.environ.get('NIMBLE_API_KEY')
API_URL = os.environ.get('API_NIMBLE_URL')


def update_contacts():
    headers = {
        'Authorization': f'Bearer {NIMBLE_API_KEY}'
    }
    response = requests.get(API_URL, headers=headers)
    contacts = response.json()['resources']

    with get_db_cursor() as cursor:
        for contact in contacts:
            if contact['fields'].get('first name'):
                fields = contact['fields']
                first_name = fields['first name'][0].get('value')
                last_name = fields['last name'][0].get('value')
                email = fields['email'][0]['value'] if fields.get('email') else None

                if email:
                    cursor.execute(
                        "INSERT INTO contacts (first_name, last_name, email) VALUES (%s, %s, %s)",
                        (first_name, last_name, email))
