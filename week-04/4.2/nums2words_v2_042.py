#!/usr/bin/env python3

import sys

numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

for line in sys.stdin:
    nums = []
    tokens = line.strip().split()
    for num in tokens:
        num = int(num)
        if num in numbers:
            nums.append(numbers[num])
        else:
            nums.append("unknown")

    print(" ".join(nums))