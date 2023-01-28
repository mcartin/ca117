#!/usr/bin/env python3

import sys

def chop(word):
    return word[1:len(word) - 1]

for line in sys.stdin:
    line = line.strip()
    chopped = chop(line)
    if chopped:
        print(chopped)
