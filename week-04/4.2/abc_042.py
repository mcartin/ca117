#!/usr/bin/env python3

import sys

tokens = sys.stdin.readline().split()
numbers = [int(t) for t in tokens]
sorted = sorted(numbers)

letter = 'ABCDEF'

z = zip(letter, sorted)

d = {k : v for k, v in z}

order = sys.stdin.readline().strip()

output = [str(d[letter]) for letter in order]
print(" ".join(output))