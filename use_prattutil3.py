#!/usr/bin/env python
import sys
#  from pratt/mil/prattutil.py ...
# from pkg.pkg.module import ....
from pratt.mil.prattutil import build_engine, design_engine

build_engine()
design_engine()

for path in sys.path:
    print(path)
