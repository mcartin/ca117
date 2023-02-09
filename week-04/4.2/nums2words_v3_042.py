#!/usr/bin/env python3

import sys

mapping = {}

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        mapping[i] = l.split()[1]

# lines = [line.split() for line in sys.stdin] if using this use for line in lines and get rid of line 24


for line in sys.stdin:
    nums = []
    tokens = line.strip().split()
    for num in tokens:
        num = int(num)
        nums.append(mapping[int(num)])
    print(" ".join(nums))