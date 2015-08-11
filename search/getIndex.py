def query( lst, index ):
    if index >= len(lst):
        return -1
    else:
        return lst[index]

def getIndex( lst, i ):
    start = 0
    end = 1
    while start < end:
        q = query( lst, end )
        if q == i:
            return end
        elif q == -1 or q > i:
            break
        else:
            assert q < i
            start = end
            end *= 2
    while start < end:
        mid = ( start + end ) / 2
        q = query( lst, mid )
        if q == -1:
            end = mid
        elif q < i:
            start = mid + 1
        else:
            end = mid
    return start


assert getIndex( [2,3,5,8,9,13,17], 8 ) == 3

import random
NUMCASES = 1000
lst = [ 2*i for i in range(100000) ]
for i in range( NUMCASES ):
    lookFor = random.randint( 5, 99995 )
    lookFor *= 2
    index = getIndex( lst, lookFor )
    assert index == lst.index( lookFor )
