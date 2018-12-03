#!/usr/bin/env python
from collections import Counter

c = Counter()

print(c['a'])
print(c['b'])
print(c)
c['a'] += 1
c['b'] += 1
print(c)


with open('DATA/breakfast.txt') as breakfast_in:
    contents = breakfast_in.read()
    food_items = contents.splitlines()
    breakfast_counts = Counter(food_items)

print(breakfast_counts)
print(breakfast_counts.most_common(3))

breakfast_counts['waffles'] += 1

more_food = ['waffles', 'waffles',  'waffles',  'waffles', 'flapjacks',  'waffles'   ]

breakfast_counts.update(more_food)
print(breakfast_counts)


