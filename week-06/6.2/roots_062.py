#!/usr/bin/env python3

import sys

def roots(a, b, c):
    a, b, c = int(a), int(b), int(c)

    D = (b * b) - (4 * a * c)
    if D < 0:
        return None
    else:
        root1 = (-b + (D ** 0.5)) / (2 * a)
        root2 = (-b - (D ** 0.5)) / (2 * a)
        big_root =  min(root1, root2)
        small_root =  max(root1, root2)

        return (f'{big_root:.1f}, {small_root:.1f}')


for line in sys.stdin:
    a, b, c = line.split()
    print(roots(a, b, c))