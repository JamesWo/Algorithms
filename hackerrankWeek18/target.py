#https://www.hackerrank.com/contests/w18/challenges/target

#!/bin/python

import sys
import math
import bisect

K,N = raw_input().strip().split(' ')
K,N = [int(K),int(N)]
R = map(int,raw_input().strip().split(' '))
x = []
for x_i in xrange(N):
   x_temp = map(int,raw_input().strip().split(' '))
   x.append(x_temp)

# for each point, binary search for which circle
# it falls in.
R = R[::-1]
points = 0
for x1, y1 in x:
    radius = math.sqrt(x1**2 + y1**2)
    # we want to insert to the right of the original R, 
    #which means insert to the left in the reversed R
    points += (len(R) - bisect.bisect_left(R, radius))
print points


