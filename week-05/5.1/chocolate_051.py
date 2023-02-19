#!/usr/bin/env python3

import sys

for line in sys.stdin:
    calories = int(line)
    chocolate = 400
    if calories % chocolate == 0:
        print(calories // chocolate)
    elif calories > 0:
        print(calories // chocolate + 1)
    else:
        print("0")
