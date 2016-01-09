#!/bin/python

# https://www.hackerrank.com/contests/hourrank-4/challenges/new-year-chaos

import sys

def solve(size, queue):
    # if any member of queue is more than 2 positions ahead of 
    # their original location, then the state is impossible
    for i in range(size):
        if queue[i] >= i+4:
            return "Too chaotic"
    # otherwise count the number of mismatched pairs - in nlogn time
    # see http://www.geeksforgeeks.org/counting-inversions/
    count = 0
    for i in range(size):
        for j in range(i+1, size):
            if queue[i] > queue[j]:
                count += 1
    return count
    
numCases = int(raw_input().strip())
for a0 in xrange(numCases):
    size = int(raw_input().strip())
    queue = map(int,raw_input().strip().split(' '))
    # your code goes here
    print solve(size, queue)

