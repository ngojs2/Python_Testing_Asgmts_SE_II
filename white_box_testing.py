# Jeffrey Ngo
# HW2: White Box Testing
# Created truth table for each conditional statements and
# tested different values to find the bugs

import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):

    # val 100-150
    def test_1(self):
        val = 120
        self.assertTrue(contrived_func(val).format(val))

    def test_2(self):
        val = 151
        self.assertFalse(contrived_func(val).format(val))

    # val * 5 < 361 and val / 2 < 24
    def test_3(self):
        val = 4
        self.assertTrue(contrived_func(val).format(val))

    def test_4(self):
        val = 60
        self.assertFalse(contrived_func(val).format(val))

    def test_5(self):
        val = 90
        self.assertFalse(contrived_func(val).format(val))

    def test_6(self):
        val = 6
        self.assertFalse(contrived_func(val).format(val))

    # > 75 and val ** val %  5 == 0
    def test_7(self):
        val = 74
        self.assertFalse(contrived_func(val).format(val))


if __name__ == '__main__':
    unittest.main()