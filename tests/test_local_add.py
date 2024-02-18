import unittest
import sys
sys.path.append('local')
from add import add


class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(5, 7)
        self.assertEqual(result, 12)

    def test_add_negative_numbers(self):
        result = add(-5, -7)
        self.assertEqual(result, -12)

    def test_add_zero(self):
        result = add(0, 0)
        self.assertEqual(result, 0)
