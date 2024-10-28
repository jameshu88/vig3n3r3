import unittest
from vig3n3r3 import encrypt, decrypt

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt(self):
        plaintext = "ATTACKATDAWN"
        key = "KEY"
        expected_ciphertext = "KXRKGIKXBKAL"
        result = encrypt(plaintext, key)
        self.assertEqual(result, expected_ciphertext)

    def test_decrypt(self):
        ciphertext = "KXRKGIKXBKAL"
        key = "KEY"
        expected_plaintext = "ATTACKATDAWN"
        result = decrypt(ciphertext, key)
        self.assertEqual(result, expected_plaintext)

if __name__ == '__main__':
    unittest.main()
