#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
for line in lines:
    count = 0 
    toprint = ''
    line = line.strip()
    current_char = line[0]
    for char in line:
        if char == current_char:
            count += 1
            current_char = char
        else:
            toprint += (str(count) + current_char)
            current_char = char
            count = 1
    toprint = toprint + (str(count) + current_char)
print(toprint)