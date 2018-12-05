#!/usr/bin/env python
import time

start_time = time.time()

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Beatrice")

print(d1)

dn = d1.get_dealer()
# dn = CardDeck.get_dealer(d1)
print(dn)

d2 = CardDeck('Amy')
print(d2.get_dealer())

print(d1.dealer_name)

d1.dealer_name = 'Horatio'

print(d1.dealer_name)

try:
    d1.dealer_name = 1.234
except TypeError as err:
    print(err)

d1.shuffle()
print(d1.cards)

hand = []
for i in range(5):
    hand.append(d1.draw())
print("hand:", hand)

print(d1.get_suits())
print(CardDeck.get_suits())

j1 = JokerDeck("Albert")

print(type(d1), type(j1))
print(dir(j1))
print()

j1.shuffle()

print(j1.cards)
j1.bark()

print(JokerDeck.mro())

print(j1.get_suits())

print(len(d1), len(j1))
print(d1, j1)

x = d1 + j1

print(x)

d2 += j1

print(d2)

end_time = time.time()

elapsed = end_time - start_time

print(f"That took {elapsed:.4f} seconds")
