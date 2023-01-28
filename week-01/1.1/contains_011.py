#!/usr/bin/env python3

import sys

for line in sys.stdin:
    #left, right = ["cat" "ccat"]
    # tokens = line.strip().lower().split()
    # left = tokens[0]
    # right = tokens[1]
    left, right = line.strip().lower().split()


    def contains(left, right):
        for letter in left:
            if letter not in right:
                return False
            else:
                right = right.replace(letter, "", 1)
        return True

    print(contains(left, right))
