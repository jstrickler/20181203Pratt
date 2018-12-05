#!/usr/bin/env python
"""
Demo script for Pratt
"""
from collections import Counter

def main():
    """
    Program entry point

    :return:
    """
    counter = Counter()

    print(counter['a'])
    print(counter['b'])
    print(counter)
    counter['a'] += 1
    counter['b'] += 1
    print(counter)


    with open('DATA/breakfast.txt') as breakfast_in:
        contents = breakfast_in.read()
        food_items = contents.splitlines()
        breakfast_counts = Counter(food_items)

    print(breakfast_counts)
    print(breakfast_counts.most_common(3))

    breakfast_counts['waffles'] += 1

    more_food = ['waffles', 'waffles', 'waffles', 'waffles', 'flapjacks', 'waffles']

    breakfast_counts.update(more_food)
    print(breakfast_counts)


if __name__ == '__main__':
    main()
