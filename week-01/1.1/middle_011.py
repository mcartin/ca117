#!/usr/bin/env

import sys

for s in sys.stdin:
    s = s.strip()
    if len(s) % 2 == 0:
        print("No middle character!")
    else:
        print(s[len(s) // 2])