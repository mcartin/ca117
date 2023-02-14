#!/usr/bin/env python3

import sys
n = sys.stdin.readline().strip()

while int(n) > 9:
    product = 1
    for i in str(n):
        if i != "0":
            product *= int(i)
    n = product
print(n)