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


if __name__ == '__main__':
    unittest.main()
