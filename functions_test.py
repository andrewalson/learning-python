import unittest
import functions


class FunctionsTest(unittest.TestCase):

    def test_reverseString_reverses_String(self):
        self.assertEqual(functions.reverseString('string'), 'gnirts')
        self.assertEqual(functions.reverseString("jute"), 'etuj')

    def test_is_word_palandrome(self):
        self.assertTrue(functions.ispal('toot'))
        self.assertFalse(functions.ispal("Palindrome"))
        self.assertTrue(functions.ispal("Hannah"))
        self.assertFalse(functions.ispal("123"))
    
    def test_prime_checker_checks_if_number_is_prime(self):
        self.assertFalse(functions.isPrime(4))
        self.assertFalse(functions.isPrime(8))
        self.assertFalse(functions.isPrime(100))
        self.assertFalse(functions.isPrime(99))
        self.assertTrue(functions.isPrime(7))
        self.assertTrue(functions.isPrime(23))
        self.assertTrue(functions.isPrime(107))
        self.assertTrue(functions.isPrime(17))