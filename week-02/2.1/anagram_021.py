#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().split()
    first = sorted(line[0])
    second = sorted(line[1])

    print(first == second)
