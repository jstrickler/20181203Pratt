#!/usr/bin/env python
from collections import defaultdict

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

fruit_info = defaultdict(list)

for fruit in fruits:
    fruit_info[fruit[0]].append(fruit)

print(fruit_info, '\n')

zero_dict = defaultdict(lambda : 0)

zero_dict['a'] = 22
zero_dict['m'] = 9
zero_dict['e'] = 55

for x in 'a', 'b', 'c', 'd', 'e', 'k', 'l', 'm':
    print(zero_dict[x])
print()
print(zero_dict)




