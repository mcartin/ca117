#!/usr/bin/env python3

import sys

for word in sys.stdin:
    i = 0
    while i < len(word) and not word[i].isnumeric():
        i += 1
    up_to_number = word[:i].split(".")
    name = up_to_number[0].capitalize()
    surname = up_to_number[1].capitalize()
    print(f"{name} {surname}")

    # print(name + " " + surname)