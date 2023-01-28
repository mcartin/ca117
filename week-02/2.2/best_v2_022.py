#!/usr/bin/env python3

import sys
filename = sys.argv[1]

try:
    highest = 0
    with open(filename) as f:
        try:
            for line in f:
                tokens = line.strip().split()
                studentmark = tokens[0]
                mark = int(tokens[0])
                
                if mark > highest:
                    highest = mark
                    name = " ".join(tokens[1:])

            print(f"Best student: {name}")
            print(f"Best mark: {highest}")

        except ValueError:
            print(f"Invalid mark {studentmark} encountered. Exiting.")

except FileNotFoundError:
    print(f"The file {filename} could not be opened.")