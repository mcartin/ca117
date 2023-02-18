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

# lines = [line.split() for line in sys.stdin] if using this use for line in lines and get rid of line 24


for line in sys.stdin:
    nums = []
    tokens = line.strip().split()
    for num in tokens:
        num = int(num)
        nums.append(numbers[num])
    print(" ".join(nums))