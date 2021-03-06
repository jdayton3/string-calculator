import unittest
from calc import string

class TestEmptyStringReturnsZero(unittest.TestCase):
    def test_empty_returns_zero(self):
        expected = 0
        actual = string("")
        self.assertEqual(actual, expected)

class TestSingleNumberReturnsValue(unittest.TestCase):
    def test_0(self):
        expected = 0
        actual = string("0")
        self.assertEqual(actual, expected)

    def test_1(self):
        expected = 1
        actual = string("1")
        self.assertEqual(actual, expected)

    def test_float(self):
        expected = 2.0
        actual = string("2.0")
        self.assertEqual(actual, expected)

    def test_not_whole_number(self):
        expected = 2.3
        actual = string("2.3")
        self.assertEqual(actual, expected)

class TestTwoNumbersNewlineDelimited(unittest.TestCase):
    def test_two_0s(self):
        expected = 0
        actual = string("0\n0")
        self.assertEqual(actual, expected)

    def test_1_2(self):
        expected = 3
        actual = string("1\n2")
        self.assertEqual(actual, expected)

    def test_1_1(self):
        expected = 2
        actual = string("1\n1")
        self.assertEqual(actual, expected)

    def test_floats(self):
        expected = 5.0
        actual = string("3.5\n1.5")
        self.assertEqual(actual, expected)

class TestNegNumbers(unittest.TestCase):
    def test_negative(self):
        self.assertRaises(ValueError, string,"-1")

if __name__ == "__main__":
    unittest.main()
