#!/usr/bin/env python3

import sys
filename = sys.argv[1]
try:
    highest = 0
    with open(filename) as f:
        for line in f:
            tokens = line.split()
            mark = int(tokens[0])

            if mark > highest:
                highest = mark
                name = " ".join(tokens[1:])
                
        print(f"Best student: {name}")
        print(f"Best mark: {highest}")

except FileNotFoundError:
    print(f"The file {filename} could not be opened.")