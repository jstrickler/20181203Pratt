#!/usr/bin/env python

#          C:DATA\mary.txt
FILE_NAME = 'DATA/mary.txt'

with open(FILE_NAME) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip() # remove \n
        print(line)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()
    print(contents) # print(str(contents))
    print(repr(contents))  # raw view
print('-' * 60)


with open(FILE_NAME) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()
    all_lines_without_nl = contents.splitlines()
    print(all_lines_without_nl)
print('-' * 60)

with open('/Users/jstrick/py/DATA/words.txt') as words_in:
    count = 0
    for line in words_in:
        if line.startswith('x'):
            count += 1
            print(line.rstrip())

print(count)
