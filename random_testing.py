# Jeffrey Ngo
# HW3: Random Testing
#
#

import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test_visa1(self):
        for i in range(0, 50000):
            card = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(card)

    def test_master1(self):
        for i in range(0, 1000):
            card = random.randint(2221000000000000, 2719999999999999)
            credit_card_validator(card)

    def test_mc1(self):
        for i in range(0, 1000):
            card = random.randint(5100000000000000, 5499999999999999)
            credit_card_validator(card)

    def test_ae1(self):
        for i in range(0, 1000):
            card = random.randint(340000000000000, 349999999999999)
            credit_card_validator(card)

    def test_am_ex1(self):
        for i in range(0, 1000):
            card = random.randint(370000000000000, 379999999999999)
            credit_card_validator(card)

    def test_length15(self):
        for i in range(0, 1000):
            card = random.randint(100000000000000, 999999999999999)
            credit_card_validator(card)

    def test_length16(self):
        for i in range(0, 1000):
            card = random.randint(1000000000000000, 9999999999999999)
            credit_card_validator(card)


if __name__ == '__main__':
    unittest.main()







