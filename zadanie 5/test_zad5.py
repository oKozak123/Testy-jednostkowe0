import unittest
from zad5 import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        #When
        result = factorial(0)

        #Then
        self.assertEqual(result, 1)

    def test_factorial_of_one(self):
        #When
        result = factorial(1)

        #Then
        self.assertEqual(result, 1)

    def test_factorial_of_positive_integer(self):
        #When
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(10), 362880)

    def test_factorial_of_negative_integer(self):
        #When
        with self.assertRaises(ValueError):
            factorial(-5)


if __name__ == "__main__":
    unittest.main()
