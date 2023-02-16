#!/usr/bin/env python3

import sys

location = sys.stdin.readline().strip()

order_to_go = sys.stdin.read().strip()


def A(list):
    tmp = list[0]
    list[0] = list[1]
    list[1] = tmp
    return list

def B(list):
    tmp = list[1]
    list[1] = list[2]
    list[2] = tmp
    return list

def C(list):
    tmp = list[0]
    list[0] = list[2]
    list[2] = tmp
    return list


prize = '123'
prize = prize.replace(location, '0')
prize_list = [char for char in prize]

for char in order_to_go:
    if char == 'A':
        prize_list = A(prize_list)
    elif char == 'B':
        prize_list = B(prize_list)
    elif char == 'C':
        prize_list = C(prize_list)

print(''.join(prize_list).index('0') + 1)