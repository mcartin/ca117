#!/usr/bin/env python3

import sys

for line in sys.stdin:
    digit, upper, lower, other = 0, 0, 0, 0

    for letter in line.rstrip():
        if letter.isnumeric():
            digit = 1
        elif letter.isupper():
            upper = 1
        elif letter.islower():
            lower = 1
        else:
            other = 1

    print(digit + upper + lower + other)