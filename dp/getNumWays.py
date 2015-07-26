def getNumWays(n):
    if not isinstance(n, int):
        raise Exception
    if n < 0:
        raise Exception
    numWays = [1, 1, 2]
    for i in range(3, n+1):
        numWays.append(
                numWays[i-1] + numWays[i-2] + numWays[i-3] 
                )
    return numWays[n]


# test

cases = {
        3:4,
        0:1,
        4:7,
        5:13,
        6:24
        }

for inp, out in cases.iteritems():
    assert getNumWays(inp) == out, "inp: %s,\nout: %s\nexpected:%s" % (
            inp, getNumWays(inp), out )
