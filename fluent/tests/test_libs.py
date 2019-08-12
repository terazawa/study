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

    def test_add(self):
        assert Vector(2, 4) + Vector(2, 1) == Vector(4, 5)

    def test_mul(self):
        assert Vector(3, 4) * 3 == Vector(9, 12)
