#!/usr/bin/env python3

import sys

def get_divisors(num):
    divisors = [n for n in range(1, num + 1) if num % n == 0]
    return divisors

def get_proper_divisors(num):
    divisors = get_divisors(num)
    divisors.remove(num)
    return divisors

def is_perfect(num):
    divisors = get_proper_divisors(num)
    return sum(divisors) == num
