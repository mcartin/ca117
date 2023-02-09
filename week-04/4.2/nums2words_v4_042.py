#!/usr/bin/env python3

import sys

numbers = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
    13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    100: "one hundred"
}

for line in sys.stdin:
    output = []
    tokens = line.strip().split()
    for num in tokens:
        if int(num) in numbers:
            output.append(numbers[int(num)])
        else:
            output.append(f"{numbers[int(num[0]) * 10]}-{numbers[int(num[1])]}")
    print(" ".join(output))