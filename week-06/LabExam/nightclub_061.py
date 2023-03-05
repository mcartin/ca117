#!/usr/bin/env python3

import sys

denied = 0
max_people = int(sys.stdin.readline())

for line in sys.stdin:
    line = line.strip().split()
    word = line[0]
    num = int(line[1])
    if word == "enter":
        if num > max_people:
            denied += 1
        else:
            max_people -= num
    elif word == "leave":
        max_people += num
    
print(denied)