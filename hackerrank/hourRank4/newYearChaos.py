#!/bin/python

import sys

def countInversions(lst):
    # divide and conquer algorithm for counting the number of
    # pairs of elements in the list which are inverted
    # This function modifies original list.
    # see http://www.geeksforgeeks.org/counting-inversions/
    return _countInversions(lst, 0, len(lst)-1)

def _countInversions(lst, left, right):
    if left >= right:
        return 0
    mid = (left + right) / 2
    count = 0
    count += _countInversions(lst, left, mid)
    count += _countInversions(lst, mid+1, right)
    count += _merge(lst, left, mid+1, right)
    return count

def _merge(lst, left, mid, right):
    count = 0
    leftIndex = left
    rightIndex = mid
    tmp = []
    while ((leftIndex <= mid-1) and (rightIndex <= right)):
        if lst[leftIndex] <= lst[rightIndex]:
            tmp.append(lst[leftIndex])
            leftIndex += 1
        else:
            tmp.append(lst[rightIndex])
            rightIndex += 1
            # the number of inversions is incremented by the number
            # of remaining elements in the left sublist
            count += (mid-leftIndex)
    tmp.extend(lst[leftIndex:mid])
    tmp.extend(lst[rightIndex:right+1])
    lst[left:right+1] = tmp
    return count
        
def countInversions2(lst):
    # O(N^2) algorithm for counting inversions, for testing purposes
    count = 0
    for i in range(size):
        for j in range(i+1, size):
            if lst[i] > lst[j]:
                count += 1
    return count
   
def solve(size, queue):
    # if any member of queue is more than 2 positions ahead of 
    # their original location, then the state is impossible
    for i in range(size):
        if queue[i] >= i+4:
            return "Too chaotic"
    # otherwise count the number of mismatched pairs - in nlogn time
    return countInversions(queue)    

    
numCases = int(raw_input().strip())
for a0 in xrange(numCases):
    size = int(raw_input().strip())
    queue = map(int,raw_input().strip().split(' '))
    # your code goes here
    print solve(size, queue)
    



