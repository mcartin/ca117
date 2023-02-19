#!/usr/bin/env python3

import sys

for line in sys.stdin:
    calories = int(line)
    calories = calories + 399
    print(calories // 400)