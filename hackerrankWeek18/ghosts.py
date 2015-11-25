"https://www.hackerrank.com/contests/w18/challenges/ghosts"

import sys
from fractions import gcd

A,B,C,D = raw_input().strip().split(' ')
A,B,C,D = [int(A),int(B),int(C),int(D)]

def ghostLivesHere(town, street, house, apt):
    return abs(town - street) % 3 == 0 and \
            (street + house) % 5 == 0 and \
            (town * house) % 4 == 0 and \
            gcd(town, apt) == 1

total = 0

for a in range(1, A+1):
    for b in range(1, B+1):
        for c in range(1, C+1):
            for d in range(1, D+1):
                if ghostLivesHere(a, b, c, d):
                    total += 1
print total


