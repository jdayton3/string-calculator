import unittest
from calc import string

class TestEmptyStringReturnsZero(unittest.TestCase):
    def test_empty_returns_zero(self):
        expected = 0
        actual = string("")
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
