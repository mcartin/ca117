#!/usr/bin/env python3

import sys


for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("m", "M", 1)
    print(line)
