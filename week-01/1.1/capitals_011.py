#!/usr/bin/env python3

import sys

def capital(word):
    return word[0].upper() + word[1:-1] + word[-1].upper()

for word in sys.stdin:
    word = word.strip()
    if len(word) > 1:
        print(capital(word))