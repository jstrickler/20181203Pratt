#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip('\n\r')
            yield line  # <1> emit next value when iterating over this

    yield "ALL DONE"


g = trimmed('../DATA/mary.txt')
for trimmed_line in g:  # <2>
    print(trimmed_line)
