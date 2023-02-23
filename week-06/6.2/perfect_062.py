#!/usr/bin/env python3

import sys

def get_divisors(num):
    divisors = []
    for n in range(1, num + 1):
        if num % n == 0:
            divisors.append(n)
    return divisors

def get_proper_divisors(n):
    divisors = get_divisors(n)
    divisors.remove(n)
    return divisors

def is_perfect(n):
    divisors = get_proper_divisors(n)
    if sum(divisors) == n:
        return True
    else:
        return False
