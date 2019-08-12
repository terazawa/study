from libs.carddeck import *
from libs.vector import *

class TestFrenchDeck:
    def setup(self):
        self._deck = FrenchDeck()

    def test_len(self):
        assert len(self._deck) == 4 * 13

    def test_getitem(self):
        assert self._deck[0] == Card(rank='2', suit='spades')

class TestVector:
    def test_abs(self):
        assert abs(Vector(3, 4)) == 5
