#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

print(len(fruits))
print(fruits[0], fruits[10], fruits[-1])
print(fruits[0:3])  # 0, 1, 2
print(fruits[5:9])  # 5, 6, 7, 8
print(fruits[-3:])  # -3, -2, -1
#  [START:STOP]  [:STOP]  [START:]
#  [START:STOP:STEP]
actress = "Kate Hudson"
print(actress[:4])
print(actress[-6:])
print(actress[1:4])

for fruit in fruits:
    print(fruit)

