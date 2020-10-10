import unittest
from roman import int_to_roman


class RomanNumeralTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual("I", int_to_roman(1))

    def test_two(self):
        self.assertEqual("II", int_to_roman(2))

    def test_three(self):
        self.assertEqual("III", int_to_roman(3))

    def test_four(self):
        self.assertEqual("IV", int_to_roman(4))

    def test_five(self):
        self.assertEqual("V", int_to_roman(5))

    def test_six(self):
        self.assertEqual("VI", int_to_roman(6))

    def test_seven(self):
        self.assertEqual("VII", int_to_roman(7))

    def test_eight(self):
        self.assertEqual("VIII", int_to_roman(8))

    def test_nine(self):
        self.assertEqual("IX", int_to_roman(9))

    def test_ten(self):
        self.assertEqual("X", int_to_roman(10))

    def test_eleven(self):
        self.assertEqual("XI", int_to_roman(11))

    def test_twelve(self):
        self.assertEqual("XII", int_to_roman(12))


if __name__ == '__main__':
    unittest.main()
