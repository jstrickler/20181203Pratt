#!/usr/bin/env python

print("Hello")

#   str bytes list tuple

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print('Guido is the "MAN"')
print("Guido's the MAN")

s3 = """Guido's the "MAN", I said"""
print(s3)

query = """
select date, part, value
from test_runs
where date > '2018-02-05'
"""

surprise = 'I ' 'have a ' 'surprise ' 'for you'

print(surprise)

q2 = (
   "select date, part, value"
    " from test_runs"
    " where date > '2018-02-05'"
)

a = "Apple"
b = b'banana'
print(type(a), type(b))

print(a.encode())
print(b.decode())

s5 = r"spam\n"

name = 'Fred Flintstone'
city = 'Bedrock'

print(f"{name} lives in {city}")  # f-string

print("{} lives in {}".format(name, city))







