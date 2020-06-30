import unittest
from flask_testing import TestCase
from app import App
from app.utilities.utils import print_test_time_elapsed


class ApiTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def create_app(self):
        self.app = App('testing').initialize()
        self.client = self.app.test_client()
        # self.baseURL = "http://localhost:5000/api/test_api"
        return self.app

    @print_test_time_elapsed
    def test_api_get(self):
        rv = self.client.get('/api/test_api')
        # assert rv.status_code == 200
        self.assertEqual(rv.status_code, 200)

    @print_test_time_elapsed
    def test_api_post(self):
        rv = self.client.post('/api/test_api')
        # assert rv.status_code == 200
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
