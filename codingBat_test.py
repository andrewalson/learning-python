import unittest
from codingBat import *


class CodingBatTest(unittest.TestCase):
    def test_pos_neg(self):
        #Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
        self.assertTrue(pos_neg(1, -1, False))
        self.assertTrue(pos_neg(-1, 1, False))
        self.assertTrue(pos_neg(-4, -5, True))

    def test_makes10(self):
        #Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
        self.assertTrue(makes10(9,10))
        self.assertFalse(makes10(9,9))
        self.assertTrue(makes10(1,9))

    def test_diff21(self):
        #Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
        self.assertEqual(diff21(19), 2)
        self.assertEqual(diff21(10), 11)
        self.assertEqual(diff21(21), 0)

    def test_front_back(self):
        #Given a string, return a new string where the first and last chars have been exchanged.
        self.assertEqual(front_back('code'), 'eodc')
        self.assertEqual(front_back('a'), 'a')
        self.assertEqual(front_back('ab'), 'ba')

    def test_front3(self):
        #Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
        self.assertEqual(front3('Java'), 'JavJavJav')
        self.assertEqual(front3('Chocolate'), 'ChoChoCho')
        self.assertEqual(front3('abc'), 'abcabcabc')