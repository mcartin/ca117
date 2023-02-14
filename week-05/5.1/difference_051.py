#!/usr/bin/env python3

import sys

line1, line2 = sys.stdin.read().split()
print(line1)
print(line2)

z = ['*' if a != b else '-' for a,b in zip(line1, line2)]
print(''.join(z))