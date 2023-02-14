#!/usr/bin/env python3

import sys
speeds = []

prevTime, prevDistance = [int(t) for t in sys.stdin.readline().strip().split()]

for lines in sys.stdin:
    curTime, curDistance = [int(t) for t in lines.strip().split()]
    speed = (curDistance - prevDistance) / (curTime - prevTime)
    speeds.append(speed)
    prevTime, prevDistance = curTime, curDistance

print(int(max(speeds)))