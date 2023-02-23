#!/usr/bin/env python3

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    horizontal_distance = x1 - x2
    vertical_distance = y1 - y2
    distance = (horizontal_distance ** 2 + vertical_distance ** 2) ** 0.5
    return (r1 + r2) > distance
