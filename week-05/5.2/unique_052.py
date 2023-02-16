#!/usr/bin/env python3

import sys



numbers = [t for t in sys.stdin.readlines()]
for n in numbers:
    num = n.split()
    uniques = [n.strip() for n in num if num.count(n) == 1]

    print(max(uniques, default='none'))