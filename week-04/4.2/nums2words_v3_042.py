#!/usr/bin/env python3

import sys

mapping = {}

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        mapping[i] = l.split()[1]

lines = [line.split() for line in sys.stdin]


for line in lines:
    nums = []
    for word in line:
            nums.append(mapping[int(word)])
    print(" ".join(nums))