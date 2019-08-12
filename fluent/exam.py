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

#%%
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print(f"{passport[0]}/{passport[1]}")

#%%
for country, _ in traveler_ids:
    print(country)

#%%
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

#%%
latitude, longitude = lax_coordinates
latitude

#%%
longitude

#%%
divmod(20, 8)

#%%
t = (20,8)
divmod(*t)

#%%
quotient, remainder = divmod(*t)
quotient, remainder

#%%
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
filename

#%%
a, b, *rest = range(5)
a, b, rest

#%%
a, b, *rest = range(3)
a, b, rest

#%%
a, b, *rest = range(2)
a, b, rest

#%%
a, *body, c, d = range(5)
a, body, c, d

#%%
metro_areas = [
    ('Tokyo', ' JP ', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', ' IN ', 21.935, (28.613889, 77.208889)),
    ('Mexico City', ' MX ', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', ' US ', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', ' BR ', 19.649, (-23.547778, -46.635833)),
]
print(f"{'-':15} | {'lat.':^9} | {'long.':^9}")
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(f"{name:15} | {latitude:9.4f} | {longitude:9.4f}")

#%%
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo

#%%
tokyo.population

#%%
tokyo.coordinates

#%%
tokyo[1]

#%%
City._fields

#%%
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict()

#%%
for key, value in delhi._asdict().items():
    print(key + ':', value)
