#!/usr/bin/env python3

import sys

for line in sys.stdin:
    numbers = [int(t) for t in line.strip().split()]
    uniques = [n for n in numbers if numbers.count(n) == 1]
    print(max(uniques, default='none'))