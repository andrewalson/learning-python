import wordreversal
import unittest

class WordReversalTest(unittest.TestCase):

    def test_determine_if_palandrome(self):
        self.assertTrue(wordreversal.palendromedoitbe('hannah'))
        self.assertFalse(wordreversal.palendromedoitbe('andrew'))


