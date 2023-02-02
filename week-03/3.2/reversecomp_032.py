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


# Build the list of words
lines = [line.strip() for line in sys.stdin]

# Build the sorted list of words (don't have to sort the list)
sorted_list = sorted([w.lower() for w in lines])

# Words whose reverse is in the list (binsearch)
reverse = [w for w in lines if len(w) >= 5 and binsearch(w[::-1].lower(), sorted_list)]

# Word whose reverse is in the list (brute-force search is too slow)
# reverse = [w for w in l if len(w) >= 5 and w[::-1].lower() in sl]

print(reverse)