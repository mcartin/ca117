#!/usr/bin/env python3

import sys
filename = sys.argv[1]
try:
    highest = 0
    names = []
    with open(sys.argv[1]) as f:
        for line in f:
            try:
                
                tokens = line.split()
                studentmark = tokens[0]
                mark = int(tokens[0])
                name = " ".join(tokens[1:])


                if mark > highest:
                    highest = mark
                    names = [name]

                elif mark == highest:
                    names.append(name)

            except ValueError:
                print(f"Invalid mark {studentmark} encountered. Skipping.")

        print(f"Best student(s): {', '.join(names)}")
        print(f"Best mark: {highest}")

except FileNotFoundError:
    print(f"The file {filename} could not be opened.")
