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

lines = [line.split() for line in sys.stdin]

for line in lines:
    nums = []
    for word in line:
            nums.append(numbers[int(word)])
    print(" ".join(nums))