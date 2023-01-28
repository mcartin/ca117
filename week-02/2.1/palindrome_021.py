#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip().lower()
    for c in line:
        if not c.isalnum():
            line = line.replace(c, "")
    print(line == line[::-1])