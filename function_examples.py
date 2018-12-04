#!/usr/bin/env python

def get_message():
    return "Hello, Pratt world"

def show_message():
    m = get_message()
    print(m)

show_message()

def add(x, y):
    return x + y


print(add(5, 10))
print(add('spam', 'ham'))

x = 8
y = 10
result = add(x, y)
print("result is", result)

def greet(*greetees):
    for greetee in greetees:
        print("Hello,", greetee)

greet('Mom')
greet('Mom', 'Dad', 'Aunt Betty')
greet()


# pos. params    req       req
def file_copy(file_name, file_folder='/tmp'):
    print("copying {} to {}".format(file_name, file_folder))


file_copy("spam.txt", "DATA")
file_copy("ham.txt")


def generic_fun(*args, **kwargs):
    print(args)
    print(kwargs)
    print("---")


generic_fun(5, 10, 15, animal='wombat', country='Romania', lake="Victoria")
generic_fun()
generic_fun(name='Bob')

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass



























