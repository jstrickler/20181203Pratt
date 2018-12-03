#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

print(len(person), person[0], person[-1])

# no can do:
# person[2] = 'Gates Foundation'

# iterable (e.g. tuple) unpacking
#  v1, v2, ... = ITERABLE
first_name, last_name, product = person


people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
    ('Ramona', 'Georgescu'),
]

print(people[0])
print(people[0][0])
print(people[0][0][0])

for p in people:
    pass


for first_name, last_name, *product in people:
    print(first_name, last_name, product)


values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

# for v1, v2, .... in ITERABLE:
#     ...

airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, name in airports.items():
    print(abbr, name)
print()

for i, n in enumerate(person):
    print(i, n)
print()

def process_person(p):
    first_name, last_name, *product = p

def add(x, y):
    return x + y







