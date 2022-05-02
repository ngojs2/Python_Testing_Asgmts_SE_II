import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    # Tests password length
    def test1(self):
        password = 'aBc23@'
        self.assertFalse(check_pwd(password))

    # Tests for uppercase letters
    def test2(self):
        password = 'asdf123@@#'
        self.assertFalse(check_pwd(password))

    # Tests for lowercase letters
    def test3(self):
        password = 'ABC123@@#'
        self.assertFalse(check_pwd(password))

    # Test for digits
    def test4(self):
        password = 'ASDFabc@@#'
        self.assertFalse(check_pwd(password))

    # Tests for symbols
    def test5(self):
        pwd = '123456abcASDF'
        self.assertFalse(check_pwd(pwd))


if __name__ == '__main__':
    unittest.main()
