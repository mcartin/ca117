#!/usr/bin/env python3


import sys

def binsearch(query, sorted_list):

    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        # print(f'{low} {mid} {high}')

        if sorted_list[mid] < query:
            # Search RHS
            low = mid + 1

        elif sorted_list[mid] > query:
            # Search LHS
            high = mid - 1

        else:
            # Found it
            return True

    # Not found
    return False


lines = [line.strip() for line in sys.stdin]

sorted_list = sorted([w.lower() for w in lines])

reverse = [w for w in lines if len(w) >= 5 and binsearch(w[::-1].lower(), sorted_list)]

print(reverse)