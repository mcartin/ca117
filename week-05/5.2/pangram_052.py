#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in line.lower():
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
    if alphabet == "":
        print("pangram")
    else:
        print(f"missing {alphabet}")
