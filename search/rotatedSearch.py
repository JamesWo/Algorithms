def rotatedSearch( arr, i ):
    if not isinstance(arr, list):
        return False
    lo = 0
    hi = len(arr)-1
    while lo < hi:
        mid = ( lo + hi ) / 2
        if ( arr[ lo ] > i and arr[ mid ] > i ): 
            lo = mid + 1
        elif ( arr[ hi ] < i and arr[ mid ] < i ):
            hi = mid
        elif arr[ mid ] < i:
            lo = mid + 1
        else:
            hi = mid
    return lo


# test

assert rotatedSearch( [1,4,6,12,16], 6 ) == 2
assert rotatedSearch( [1,4,6,12,16], 16 ) == 4
assert rotatedSearch( [1,4,6,12,16], 1 ) == 0
assert rotatedSearch( [12,16,1,4,6], 12 ) == 0
assert rotatedSearch( [12,16,1,4,6], 16 ) == 1
assert rotatedSearch( [12,16,1,4,6], 1 ) == 2
assert rotatedSearch( [12,16,1,4,6], 4 ) == 3
assert rotatedSearch( [12,16,1,4,6], 6 ) == 4
assert rotatedSearch( [16,1,4,6,12], 6 ) == 3

import random
NUMCASES = 1
lst = [ i for i in range(100) ]
for i in range( NUMCASES ):
    # rotate the list by some amount
    amount = random.randint( 5, 95 )
    lst = lst[amount:] + lst[:amount]
    lookFor = random.randint( 5, 95 )
    index = rotatedSearch( lst, lookFor )
    if index != lst.index( lookFor ):
        import pdb; pdb.set_trace()
