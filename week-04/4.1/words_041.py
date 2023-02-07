#!/usr/bin/env python3

import sys
import string
counter = {}
# banned = '!"#$%&()*+, -./:;<=>?@[\]^_`{|}~'
banned = string.punctuation
banned = banned.replace("'", "")

for words in sys.stdin.read().split():
    words = words.lower()
    for ch in words:
        if ch in banned:
            words = words.replace(ch, "")
    if words not in counter:
        counter[words] = 1
    else:
        counter[words] += 1

for k, v in sorted(counter.items()):
    print(f"{k} : {v}")