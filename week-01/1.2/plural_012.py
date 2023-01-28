#!/usr/bin/env python3

import sys

vowels = "aeiou"
ending = ["ch", "sh", "x", "s", "z"]

for noun in sys.stdin:
    noun = noun.strip()
    if noun[-1:] in ending or noun[-2:] in ending:
        print(f"{noun}es")
    elif noun[-2] not in vowels and noun[-1] == "y":
        print(f"{noun[:-1]}ies")
    elif noun[-1] == "f":
        print(f"{noun[:-1]}ves")
    elif noun[-2:] == "fe":
        print(f"{noun[:-2]}ves")
    elif noun[-1] == "o":
        print(f"{noun}es")
    else:
        print(f"{noun}s")


# for noun in sys.stdin:
#     noun = noun.strip()
#     if noun[-1:] in ending or noun[-2:] in ending:
#         print(noun + "es")
#     elif noun[-2] not in vowels and noun[-1] == "y":
#         print(noun[:-1] + "ies")
#     elif noun[-1] == "f":
#         print(noun[:-1] + "ves")
#     elif noun[-2:] == "fe":
#         print(noun[:-2] + "ves")
#     elif noun[-1] == "o":
#         print(noun + "es")
#     else:
#         print(noun + "s")
