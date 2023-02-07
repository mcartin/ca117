#!/usr/bin/env python3

import sys

contacts = {}

with open(sys.argv[1]) as f:
    for line in f:
        [name, num, email] = line.split()
        contacts[name] = (num, email)

for name in sys.stdin:
    name = name.strip()
    if name in contacts:
        print(f'Name: {name}')
        print(f'Phone: {contacts[name][0]}')
        print(f'Email: {contacts[name][1]}')
    else:
        print(f'Name: {name}')
        print("No such contact")