from unittest import TestCase
import unittest
from zad1 import file_sumer


class Test(unittest.TestCase):

    def test_non_existing_file(self):
        # Given
        file = 'file path not exist'

        # When
        with self.assertRaises(FileNotFoundError):
            result = file_sumer(file)
            return result

    def test_empty_file(self):
        # Given
        file = 'test2.txt'
        expected = 0

        # When
        result = file_sumer(file)

        # Then
        self.assertEqual(expected, result)

    def test_all_in_range(self):
        # Given
        file = 'test3.txt'
        expected = 6

        # When
        result = file_sumer(file)

        # Then
        self.assertEqual(expected, result)

    def test_out_of_range(self):
        # Given
        file = 'test4.txt'

        # When
        with self.assertRaises(ValueError):
            result = file_sumer(file)

    def test_only_plain_text(self):
        # Given
        file = 'test5.txt'

        # When
        with self.assertRaises(TypeError):
            result = file_sumer(file)

        # Then
        # (Assert statement is in the 'when' block)


if __name__ == '__main__':
    unittest.main()
