#%% [markdown]
## Exsample 1-1

#%%
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

#%%
beer_card = Card('7', 'diamonds')
beer_card

#%%
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, positoin):
        return self._cards[positoin]

#%%
deck = FrenchDeck()
len(deck)

#%%
deck[0]

#%%
deck[-1]

#%%
from random import choice

#%%
choice(deck)

#%%
deck[:3]

#%%
deck[12::13]

#%%
for card in deck:
    print(card)

#%%
for card in reversed(deck):
    print(card)
