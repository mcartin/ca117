#!/usr/bin/env python3

import sys


d = {}
animals = []
for line in sys.stdin:
    line = line.strip().split()
    for word in line:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
occurence = max(d.values())
for k, v in sorted(d.items()):
    if v == occurence:
        animals.append(k)

print(len(animals))
for i in animals:
    print(i)
