#!/usr/bin/env python
import unittest
from carddeck import CardDeck
import tempfile
import sys

TEST_USER = "Test User"

class TestCardDeck(unittest.TestCase):

    def setUp(self):
        self.d = CardDeck(TEST_USER)

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @unittest.skipUnless(sys.platform == 'win32', "Only implemented on Windows")
    def test_deck_has_52_cards(self):
        self.assertEqual(52, len(self.d), "Deck does NOT have 52 cards")

    def test_deal_one_card_reduces_len_by_one(self):
        old_len = len(self.d)
        self.d.draw()
        new_len = len(self.d)
        self.assertEqual(old_len - 1, new_len, "Drawing one card does not reduce length")

if __name__ == '__main__':
    unittest.main()

