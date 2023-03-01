#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    count = line.count("e")
    count = count * 2
    print("h" + (count * "e") + "y")