#!/usr/bin/env python3

import sys

contacts = {}
filename = sys.argv[1]

with open(filename) as f:
    for line in f:
        name, num = line.split()
        contacts[name] = num

for name in sys.stdin:
    name = name.strip()
    if name in contacts:
        print(f'Name: {name}')
        print(f'Phone: {contacts[name]}')
    else:
        print(f'Name: {name}')
        print("No such contact")