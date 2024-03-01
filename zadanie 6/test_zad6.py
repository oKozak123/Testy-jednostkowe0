import unittest
from zad6 import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_positive_shift(self):
        #Given
        plaintext = "Hello, World!"
        shift = 3

        #When
        encrypted_text = caesar_cipher(plaintext, shift)

        #Then
        self.assertEqual(encrypted_text, "Khoor, Zruog!")

    def test_encrypt_negative_shift(self):
        #Given
        plaintext = "Hello, World!"
        shift = -3

        #When
        encrypted_text = caesar_cipher(plaintext, shift)

        #Then
        self.assertEqual(encrypted_text, "Ebiil, Tloia!")

    def test_encrypt_with_float_key(self):
        #Given
        plaintext = "Hello, World!"
        float_shift = 2.5

        #Then
        with self.assertRaises(ValueError):
            caesar_cipher(plaintext, float_shift)

if __name__ == "__main__":
    unittest.main()
