#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
for line in lines:
    count = 0 
    toprint = ''
    line = line.strip()
    c = line[0]
    for char in line:
        if char == c:
            count += 1
            c = char
        else:
            toprint += (str(count) + c)
            c = char
            count = 1
    toprint = toprint + (str(count) + c)
print(toprint)