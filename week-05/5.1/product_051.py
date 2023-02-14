#!/usr/bin/env python3

import sys

n = sys.stdin.readline().strip()

while int(n) > 9:
    n = str(n)
    nums = [int(i) for i in n]
    product = 1
    for i in nums:
        if i != 0:
            product *= i
    n = product
print(n)