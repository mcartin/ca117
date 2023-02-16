#!/usr/bin/env python3

import sys

def strike(tokens):
    return sum([int(t) for t in tokens])
    

def sorter(t):
    return t[1]


dict = {}
disqualified = []
for line in sys.stdin:
    tokens = line.strip().split()
    name = ' '.join(tokens[:-3])
    try:
        dict[name] = strike(tokens[-3:])
    except ValueError:
        	disqualified.append(name)
for k, v in sorted(dict.items(), key=sorter):
    print(f'{k:s}: {v:d}')
if disqualified:
    print(f'Disqualified: {", ".join(disqualified):s}')