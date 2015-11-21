"""
Problem Statement

Bob is in a candy shop and wants to purchase his favorite candy, which he knows costs N dollars. He has an infinite number of 1,2,5,10,20,50, and 100 dollar bills in his pocket. Bob wants to know the number of different ways he can pay the N dollars for his candy.

Input Format

A single integer, N, which is the cost of Bob's candy.

Constraint
1≤N≤250

Output Format

Print an integer representing the number of different variations of how Bob can pay.
"""
#!/bin/python

import sys


N = int(raw_input().strip())
# your code goes here
bills = [1,2,5,10,20,50,100]
cache = {}
def numWays(n, upTo):
    orign = n
    if (n, upTo) in cache:
        return cache[(n, upTo)]
    if n == 0:
    #    cache[(n, upTo)] = 1
        return 1
    if upTo == 0:
    #    cache[(n, upTo)] = 1
        return 1    
    total = numWays(n, upTo-1)
    while n >= bills[upTo]:
        n -= bills[upTo]
        total += numWays(n, upTo-1)
    cache[(orign, upTo)] = total
    return total
    
print numWays(N, 6)
    
