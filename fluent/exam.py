#%%
import collections
from libs.carddeck import *
from libs.vector import *

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

#%%
v = Vector(3,4)
v

#%%
abs(v)

#%%
Vector(2, 1) + Vector(2, 4)

#%%
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
codes

#%%
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii

#%%
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
tshirts

#%%
tuple(ord(symbol) for symbol in symbols)

#%%
import array
a = array.array('I', (ord(symbol) for symbol in symbols))
for i in a:
    print(f"{i} : {type(i)}")

#%%
for tshirts in ( f"{c} {s}" for c in colors for s in sizes):
    print(tshirts)
