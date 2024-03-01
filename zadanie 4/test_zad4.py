import unittest
from zad4 import is_prime

class TestIsPrime(unittest.TestCase):

    def test_negative_number(self):
        #When
        result = is_prime(-5)

        #Then
        self.assertFalse(result)

    def test_zero(self):
        #When
        result = is_prime(0)

        #Then
        self.assertFalse(result)

    def test_one(self):
        #When
        result = is_prime(1)

        #Then
        self.assertFalse(result)

    def test_prime_number(self):
        #Then
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))

    def test_non_prime_number(self):

        #Then
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))


if __name__ == "__main__":
    unittest.main()
