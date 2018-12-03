#!/usr/bin/env python
from collections import namedtuple
from pprint import pprint

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

Person = namedtuple('Person', 'first_name last_name product')

p = Person('Ramona', 'Georgescu', 'Scripts')

print(p)
print(p[0], p[1])
print(p.first_name, p.last_name)
print()

persons = [Person(*p) for p in people]
for person in persons:
    print(person.first_name, person.last_name, person[0])
print()

person = Person('Larry', 'Page', 'Google')
print(person.last_name)

persons[-2] = persons[-2]._replace(last_name='Chapter')
print(persons[-2])


pprint(persons)






