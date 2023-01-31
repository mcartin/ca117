#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = [int(n) for n in range(2, (int(line) + 1))]
    primes = [n for n in nums if all(n % k != 0 for k in range(2, n))]
    print(f"Primes: {primes}")