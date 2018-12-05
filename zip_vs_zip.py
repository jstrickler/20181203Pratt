#!/usr/bin/env python
from timeit import Timer

setup1 = """
from zipfile import ZipFile
import os.path
import glob
file_names = glob.glob('DATA/*')

"""

code1 = """
z = ZipFile("benchmark2 .zip", "w")
for file_name in file_names:
    z.write(file_name)
"""

setup2 = """
from shutil import create_archive
"""

code2 = """
create_archive('benchmark2.zip', 'zip', 'DATA')
"""

t1 = Timer(code1, setup1)
print(t1.timeit(1000))

t2 = Timer(code2, setup2)
print(t1.timeit(1000))
