#!/usr/bin/env python3

import sys

for line in sys.stdin:
    A, B = line.lower().split()
    a_index = 0
    b_index = 0

    #find the index the letter in common of both words in A
    for i in range(len(A)):
        if A[i] in B:
            a_index = i

    #find the index the letter in common of both words in A
    for i in range(len(B)):
        if B[i] == A[a_index]:
            b_index = i

first = "." * b_index
leftover = "." * (len(B) - b_index - 1)
for i in range(len(A)):
    if i == a_index:
        print(B)
    else:
        print(first + A[i] + leftover)