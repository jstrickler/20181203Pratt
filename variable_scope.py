#!/usr/bin/env python

x = 100 # global var
z = 'zebra'

for i in range(5):
    print(i)



def spam():
    x = "toast"
    y = 10  # local var
    print(x)

    def ham():
        print(y)

    ham()


spam()

print(x)
# print(y)
