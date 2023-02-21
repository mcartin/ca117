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
    if len(token) > 0 and token not in unique:
    # if token not in unique and token.isalnum():
      unique.append(token)
print(len(unique))
