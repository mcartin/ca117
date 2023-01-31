#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = int(line)
    r = range(1, nums + 1)
    output = [0 if n % 3 else n for n in r]
    # output = [0 if not n % 3 == 0 else n for n in r]
    print(f"Non-multiples of 3 replaced: {output}")