#!/usr/bin/env python

value = 56

if value > 75:
    print("wombat")
elif value > 50:
    print("kookaburra")
else:
    print("crocodile")

#  A?B:C
#  B if A else C
color = 'blue' if value > 50 else 'red'

animals = ['wombat', 'crocodile', 'wallaby']

for animal in animals:
    print(animal)
print()

# pseudocode
# animal = animals[0]
# do body
# animal = animals[1]
# do body

# BAD PROGRAMMER! NO BISCUIT!
# for i in range(length(animals)):
#     print(animals[i])

for i, animal in enumerate(animals):
    print(i, animal)

print(list(enumerate(animals, 1)))


for i, animal in enumerate(sorted(animals), 100):
    print(i, animal)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

target = 'a'

for fruit in fruits:
    if fruit.startswith(target):
        print(fruit)
        break
else:
    print("not found")


# while True:
#     user_name = input("What is your name? ")
#     if user_name == 'q':
#         break
#     if user_name == '':
#         continue
#     print(f"Welcome, {user_name}")

