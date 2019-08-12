#%% [markdown]
## Exsample 1-1

#%%
import collections
from libs import *

#%%
beer_card = Card('7', 'diamonds')
beer_card

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

#%%
Card('Q', 'hearts') in deck

#%%
Card('7', 'beasts') in deck

#%%
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
spades_high(Card('Q', 'hearts'))

Card('7', 'spades')
