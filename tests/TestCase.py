import unittest
import json
from app import app


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_search_contacts_if_present(self):
        response = self.app.get('/search?q=oleg')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)

        first_contact = data[0]
        self.assertTrue('id' in first_contact)
        self.assertTrue('first_name' in first_contact)
        self.assertTrue('last_name' in first_contact)
        self.assertTrue('email' in first_contact)

    def test_search_contacts_no_query(self):
        response = self.app.get('/search')
        data = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 0)
