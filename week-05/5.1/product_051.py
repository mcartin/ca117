#!/usr/bin/env python3

from sys import stdin

n = stdin.readline().strip()
while 9 < int(n):
    n = str(n)
    nums = [int(i) for i in n]
    product = 1
    for i in nums:
        if i != 0:
            product *= i
    n = product

print(n)