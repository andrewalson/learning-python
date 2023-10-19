import unittest
from findminimum import *
class findminimum_test(unittest.TestCase):
    def test_findminimum_findsminimum(self):
        notmylist = [2, 4, 7, 1, 77, 32, -1]
        self.assertEqual(findminimum(notmylist),-1)

        notmylist = [77, 33, 55, 11, 99, 88, -22]
        self.assertEqual(findminimum(notmylist),-22)