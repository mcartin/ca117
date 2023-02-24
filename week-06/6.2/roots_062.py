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
        root1 = round(root1, 1)
        root2 = round(root2, 1)

        return (f'{min(root1, root2)}, {max(root1, root2)}')
        # if root1 > root2:
        #     return (f'{root2}, {root1}')
        # else:
        #     return (f'{root1}, {root2}')
        

for line in sys.stdin:
    a, b, c = line.split()
    print(roots(a, b, c))