def nextHighest(i):
    c0 = 0
    c1 = 0
    while (i>0 and (i&1)==0):
        c0 += 1
        i >>= 1
    while ((i&1)==1):
        c1 += 1
        i >>= 1
    if c1 == 0:
        # no 1s in the original number
        return 0
    i |= 1
    i <<= ( c0 + c1 )
    i |= ((1<<(c1-1))-1)
    return i

inp = '11011001111100'
exp = '11011010001111'

res = nextHighest( int( inp, 2 ) )
assert res == int( exp, 2 ), "%s %s" % ( bin(res), exp )

assert nextHighest(3) == 5
assert nextHighest(0) == 0

