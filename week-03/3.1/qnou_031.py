#!/usr/bin/env python3

import sys

def isQnou(c):
    c = c.lower().replace("qu", "")
    return "q" in c

output = [c.strip() for c in sys.stdin if isQnou(c)]

print(f"Words with q but no u: {output}")