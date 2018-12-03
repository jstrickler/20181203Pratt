#!/usr/bin/env python

x = 5

print(x)

y = x

x = 22

print(x, y)

y = 'potato'

colors = ['red', 'blue', 'green']

c2 = colors

c2.append('purple')

print(colors)

c3 = list(colors)

c4 = colors[:]

print(id(colors), id(c2), id(c3), id(c4))

m = 5
n = 5
j = 5

print(id(m), id(n), id(j))

a1 = "apple"
a2 = "apple"

v1 = None

print(type(x), type(a1), type(v1))

def spam():
    pass

print(type(spam))

import re

print(type(re))

#    a-z A-Z 0-9 _

#  target_value   not    tval








