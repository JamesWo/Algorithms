def getNumWays(n):
    if not isinstance(n, int):
        raise Exception
    if n < 0:
        raise Exception
    numWays = [0, 1, 2]
    for i in range(3, n+1):
        numWays.append(
                numWays[i-1] + 2*numWays[i-2] + 4*numWays[i-3] 
                )
    return numWays[n]


# test

cases = {
        3:4,
        0:0,
        }

for inp, out in cases.iteritems():
    assert getNumWays(inp) == out
