#!/usr/bin/env python3

import sys

for line in sys.stdin:
    calories = int(line)
    calories = calories + 300
    print(calories // 400)
