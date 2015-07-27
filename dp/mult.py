def mult(a, b):
    """
    multiply two numbers with only +, -, and bit shifts.
    """
    signFlip = False
    if a < 0:
        a = -a
        signFlip = not signFlip
    if b < 0:
        b = -b
        signFlip = not signFlip
    total = 0
    while b > 0:
        if ( b & 1 ):
            total += a
        b >>= 1
        a <<= 1
    if signFlip:
        total = -total
    return total

# more optimized version, for when b has lots of zeros
import math
def mult2(a, b):
    """
    multiply two numbers with only +, -, and bit shifts.
    """
    signFlip = False
    if a < 0:
        a = -a
        signFlip = not signFlip
    if b < 0:
        b = -b
        signFlip = not signFlip
    total = 0
    while b > 0:
        # get the index of the right-most 1
        shift = int( math.log( b & -b, 2 ) )
        b >>= shift
        a <<= shift
        total += a
        b >>= 1
        a <<= 1
    if signFlip:
        total = -total
    return total



# test

def testMultiply(a, b, func):
    result = func(a, b)
    expected = a * b
    if result != expected:
        print "failed multiply( %d, %d )" % (a, b)
        print "expected: ", expected
        print "result: ", result
        assert False

import random
NUMCASES = 10000
for i in range(NUMCASES):
    testMultiply( random.randint(-100000, 100000),
                  random.randint(-100000, 100000),
                  mult )

    testMultiply( random.randint(-100000, 100000),
                  random.randint(-100000, 100000),
                  mult2 )


