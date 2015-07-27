def containsMagic(lst):
    """
    returns True iff some index i in lst satisfies lst[i]==i
    """
    assert isinstance(lst, list)
    lo = 0
    hi = len(lst)-1
    while lo<hi:
        mid = (lo+hi)/2
        if lst[mid]==mid:
            return True
        if lst[mid] > mid:
            hi = mid-1
        if lst[mid] < mid:
            lo = mid+1
    return lst[lo]==lo

# test

cases = {
        (-1,2,3,4,5,6):False,
        (-2,-1,0,2,4,6,8,9,10,11,12,13,14,15,16,23,45,99):True,
        (-3,0,2,3,4,6,9):True,
        (-3,0,1,4,5,6,7,8,9,10,12,13,15):False,
        (0,1,2,3,4,5,6):True
        }

for inp, out in cases.iteritems():
    lst = list(inp)
    result = containsMagic(lst)
    if result != out:
        print "input: ",lst
        print "result: ",result
        print "expected: ",out
        assert False

# test
import random
import math
def testOnce():
    lst = [random.randint(-10000,1)]
    for i in range(1,random.randint(5,5000)):
        lo = lst[i-1]
        lst.append(random.randint(lo+1, math.floor(1.2*i)))
    #print "testing on lst:", lst
    result = containsMagic(lst)
    # linear search
    trueResult = False
    for i in range(len(lst)):
        if lst[i] == i:
            trueResult=True
            break
    assert result == trueResult
    return result

# make sure we get a good number of True and False test cases

NUMTESTS = 1000
trueCount = 0
for i in range(NUMTESTS):
    if testOnce():
        trueCount += 1

print "%d/%d tests returned True" % (trueCount, NUMTESTS)
