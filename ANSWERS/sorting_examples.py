#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print("f0", f0, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n0 = sorted(nums)
print("n0", n0, '\n')

x = "spam"
print(x.lower())

print(str.lower(x))
print(str.count(x, 'm'))

print(str.lower)

f1 = sorted(fruits, key=str.lower)
print("f1:", f1, '\n')

f2 = sorted(fruits, key=len)
print("f2:", f2, '\n')

def custom_sort(element):
    return len(element), element.lower()

f3 = sorted(fruits, key=custom_sort)
print('f3:', f3, '\n')

more_nums = [5, 8, 1, "19", 4, 81, 300, 55, "abc"]
mn1 = sorted(more_nums, key=str)
print("mn1:", mn1, '\n')

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

for person in sorted(people):
    print(person)
print()

def by_last_name(person):
    return person[1], person[0]

for person in sorted(people, key=by_last_name):
    print(person)
print()

def wacky(e):
    return e[-1]

f4 = sorted(fruits, key=wacky)
print("f4:", f4, '\n')

for person in sorted(people, key=lambda e: (e[1], e[0])):
    print(person)
print()

