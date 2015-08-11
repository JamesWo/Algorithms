def mergeSortHelper(lst, start, end):
    if ( end - start ) < 1:
        return
    mid = start + ( ( end - start ) / 2 )
    mergeSortHelper( lst, start, mid )
    mergeSortHelper( lst, mid+1, end )
    tmp = lst[ : ]
    curr = start
    i1 = start
    i2 = mid + 1
    while ( i1 <= mid and i2 <= end ):
        if tmp[ i1 ] <= tmp[ i2 ]:
            lst[ curr ] = tmp[ i1 ]
            i1 += 1
        else:
            lst[ curr ] = tmp[ i2 ]
            i2 += 1
        curr += 1
    while i1 <= mid:
        assert i2 == ( end + 1 )
        lst[ curr ] = tmp[ i1 ]
        i1 += 1
        curr += 1
    while i2 <= end:
        assert i1 == ( mid + 1 )
        lst[ curr ] = tmp[ i2 ]
        i2 += 1
        curr += 1

def mergeSort(lst):
    mergeSortHelper(lst, 0, len(lst) - 1 )
    return lst

# test

# since python list.sort() is optimized (using C, aka cheating),
# lets write a naive 
# O(n^2) sorting algorithm to compare against
# use list.sort() to verify our results

def insertionSort(lst):
    index = 0
    while index < len(lst):
        curr = index
        smallest = lst[curr]
        smallestIndex = curr
        while curr < (len(lst)-1):
            curr += 1
            if lst[curr] < smallest:
                smallest = lst[curr]
                smallestIndex = curr
        # swap index with smallest
        tmp = lst[index]
        lst[index] = smallest
        lst[smallestIndex] = tmp
        index += 1

assert mergeSort( [1,2,3] ) == [1, 2, 3]
assert mergeSort( [3,2,1] ) == [1, 2, 3]
assert mergeSort( [3,1,2] ) == [1, 2, 3]

import random
import time
NUMTESTS = 2
inpSize = 10000

mergeSortTimes = []
insertionSortTimes = []
systemSortTimes = []
inputSizes = []

for _ in range(NUMTESTS):
    # generate random array
    inp = [ random.randint( 0, 10*inpSize ) for i in range( random.randint( inpSize, 2*inpSize) ) ]
    inputSizes.append( len( inp ) )
    inpCopy = inp[:]
    inpCopy2 = inp[:]

    before = time.time()
    mergeSort(inp)
    after = time.time()
    mergeSortTimes.append( after - before )

    before = time.time()
    insertionSort(inpCopy2)
    after = time.time()
    insertionSortTimes.append( after - before )
    
    before = time.time()
    inpCopy.sort()
    after = time.time()
    systemSortTimes.append( after - before )

    assert inp == inpCopy == inpCopy2

print "average input size: %f" % ( sum( inputSizes ) / NUMTESTS )
print "Average mergeSort time: %f seconds" % ( sum( mergeSortTimes ) / NUMTESTS )
print "Average insertionSort time: %f seconds" % ( sum( insertionSortTimes ) / NUMTESTS )
print "Average system sort time: %f seconds" % ( sum( systemSortTimes ) / NUMTESTS )
