import unittest
from findpezos import *
class findpezos_test(unittest.TestCase):
    def test_findnumberofpezos_findtotalnumofpezos(self):
        names = ['gates', 3, 'buffet', 'pezos', 1, 'amateurs', 'pezos', 'suckit', 2, 'pezos']
        self.assertEqual(findpezos(names),3)

        names = ['pezos', 3, 'buffet', 'pezos', 1, 'amateurs', 'pezos', 'suckit', 2, 'pezos']
        self.assertEqual(findpezos(names),4)

    def test_findindexofpezos_findsfirstindexofpezos(self):
        names = ['gates', 3, 'buffet', 'pezos', 1, 'amateurs', 'pezos', 'suckit', 2]
        self.assertEqual(findindexofpezos(names),3)

        names = ['gates', 3, 'buffet', 1, 'amateurs', 'pezos', 'suckit', 2, 'pezos']
        self.assertEqual(findindexofpezos(names),5)