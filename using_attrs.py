#!/usr/bin/env python

import attr

@attr.s
class Coordinates(object):
    x = attr.ib()
    y = attr.ib()

c = Coordinates(5, 10)

print(c)

