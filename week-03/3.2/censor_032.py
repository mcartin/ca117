#!/usr/bin/env python3

import sys
textfile = sys.argv[1]


with open(textfile) as f:
    censor = [line.strip() for line in f.readlines()]

text = [word.strip() for word in sys.stdin]

for words in text:
    for censored in censor:
        if censored in words:
            words = words.replace(censored, "@" * len(censored))
    print(words)