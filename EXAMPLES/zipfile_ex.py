#!/usr/bin/env python

from zipfile import ZipFile, ZIP_DEFLATED
import os.path
from pprint import pprint
from shutil import move, make_archive

# reading & extracting
rzip = ZipFile("../DATA/textfiles.zip")  # <1>
print(rzip.namelist())  # <2>
ty = rzip.read('tyger.txt').decode()  # <3>
print(ty[:50])
rzip.extract('parrot.txt')  # <4>

# creating a zip file
wzip = ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED)  # <5>
for base in "parrot tyger knights alice poe_sonnet spam".split():
    filename = os.path.join("../DATA", base + '.txt')
    print("adding {} as {}".format(filename, base + '.txt'))
    wzip.write(filename, base + '.txt')  # <6>

zshaun = ZipFile("../shaun.zip")
print(zshaun)
pprint(zshaun.namelist())

with open("/tmp/betsy.txt", "wb") as betsy_out:
    betsy_out.write(zshaun.read("foo/bar/blah/spam/ham/toast/jam/waffles/alice.txt"))

target = "foo/bar/blah/spam/ham/toast/jam/waffles/alice.txt"
zshaun.extract(target)
move(target, os.path.basename(target))

make_archive("spam", "zip", "spam")



