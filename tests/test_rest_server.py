import unittest
import sys
sys.path.append('rest')
from server import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add_numbers(self):
        response = self.app.get('/add?num1=5&num2=7')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 12)

    def test_add_negative_numbers(self):
        response = self.app.get('/add?num1=-5&num2=-7')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], -12)

    def test_add_zero(self):
        response = self.app.get('/add?num1=0&num2=0')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 0)
