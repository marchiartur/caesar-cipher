import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_first_alphabet_letter_moving_one_letter(self):
        self.assertEqual(caesarCipher.encryptString("a", 1), "b")

    def test_encrypt_last_alphabet_letter_moving_one_letter(self):
        self.assertEqual(caesarCipher.encryptString("z", 1), "a")

    def test_encrypt_set_string_moving_four_letters(self):
        self.assertEqual(caesarCipher.encryptString("this is a message to be encrypted", 4), "xlmw mw e qiwweki xs fi irgvctxih")

if __name__ == '__main__':
    unittest.main()
