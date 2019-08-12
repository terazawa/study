from libs.carddeck import *

class TestLibs:
    def setup(self):
        self._deck = FrenchDeck()

    def test_len(self):
        assert len(self._deck) == 4 * 13

    def test_getitem(self):
        assert self._deck[0] == Card(rank='2', suit='spades')
