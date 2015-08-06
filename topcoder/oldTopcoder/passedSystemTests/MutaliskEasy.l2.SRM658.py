# http://community.topcoder.com/stat?c=problem_statement&pm=13782

import math
import pdb

def solveTwo(hps):
    costs = [[0 for _ in xrange(hps[1]+1)] for __ in xrange(hps[0]+1)]
    for row in range(hps[0]+1):
        for col in range(hps[1]+1):
            if row == col == 0:
                continue
            c1 = costs[ max(0, row-9) ][ max(0, col-3) ]
            c2 = costs[ max(0, row-3) ][ max(0, col-9) ]
            costs[row][col] = min(c1, c2) + 1
    return costs[hps[0]][hps[1]]

def solveThree(hps):
    costs = [[[0 for _2 in xrange(hps[2]+1)] for _1 in xrange(hps[1]+1)] for _0 in xrange(hps[0]+1)]
    for i in range(hps[0]+1):
        for j in range(hps[1]+1):
            for k in range(hps[2]+1):
                if i == j == k == 0:
                    continue
                c1 = costs[ max(0, i-9) ][ max(0, j-3) ][ max(0, k-1) ]
                c2 = costs[ max(0, i-9) ][ max(0, j-1) ][ max(0, k-3) ]
                c3 = costs[ max(0, i-3) ][ max(0, j-9) ][ max(0, k-1) ]
                c4 = costs[ max(0, i-3) ][ max(0, j-1) ][ max(0, k-9) ]
                c5 = costs[ max(0, i-1) ][ max(0, j-9) ][ max(0, k-3) ]
                c6 = costs[ max(0, i-1) ][ max(0, j-3) ][ max(0, k-9) ]
                costs[i][j][k] = min(c1, c2, c3, c4, c5, c6) + 1
    return costs[hps[0]][hps[1]][hps[2]]

class MutaliskEasy(object):
    def minimalAttacks(self, hps):
        if len(hps) == 1:
            return math.ceil( hps[0] / 9.0 )
        if len(hps) == 2:
            return solveTwo(hps)
        if len(hps) == 3:
            return solveThree(hps)
        assert False, "hps contains more than 3 elements"

# test

inp = [ [12, 10, 4], [54, 18, 6], [55, 60, 53], [1,1,1], [60,40], [60] ]
out = [ 2,           6,           13,           1,       9,       7    ]

assert len(inp) == len(out)

tester = MutaliskEasy()

for i in range(len(inp)):
    result = tester.minimalAttacks(inp[i])
    expected = out[i]
    if result != expected:
        print "Failed"
        import pdb
        pdb.set_trace()
    else:
        print "pass %d" % i
