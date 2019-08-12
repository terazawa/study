#%%
import collections
from libs.carddeck import *

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
spades_high(Card('Q', 'hearts'))

#%%
Card('7', 'spades')

#%%
for card in sorted(deck, key=spades_high):
    print(card)
