#!/bin/python
import sys

n = int(raw_input().strip())
times = map(int,raw_input().strip().split(' '))
times.sort()
queueLen = 0
lastArrival = 0
latestTime = 0
for arrivalTime in times:
    if arrivalTime == lastArrival:
        queueLen += 1
    else:
        queueLen -= (arrivalTime-lastArrival-1)
        queueLen = max(0, queueLen)
        lastArrival = arrivalTime
    latestTime = max(latestTime, lastArrival+queueLen)
print latestTime
