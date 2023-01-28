#!/usr/bin/env python3

import sys
import string

tokens = sys.stdin.read().split()
unique = []
for token in tokens:
    token = token.lower().strip()
    for char in token:
        if char in string.punctuation:
         token = token.replace(char, "")
    if token.isalnum() and token not in unique:
    # if token not in unique and len(token) > 0:
      unique.append(token)
print(len(unique))
