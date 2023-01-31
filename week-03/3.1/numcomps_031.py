#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = [int(n) for n in range(1, int(line) + 1)]

    mul_3 = [n for n in nums if n % 3 == 0]
    mul_3_sq = [n * n for n in nums if n % 3 == 0]
    mul_4_double = [n * 2 for n in nums if n % 4 == 0]
    mul_3_or_4 = [n for n in nums if n % 3 == 0 or n % 4 == 0]
    mul_3_and_4 = [n for n in nums if n % 3 == 0 and n % 4 == 0]


    print(f"Multiples of 3: {mul_3}")
    print(f"Multiples of 3 squared: {mul_3_sq}")
    print(f"Multiples of 4 doubled: {mul_4_double}")
    print(f"Multiples of 3 or 4: {mul_3_or_4}")
    print(f"Multiples of 3 and 4: {mul_3_and_4}")