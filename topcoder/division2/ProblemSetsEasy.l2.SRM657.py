# http://community.topcoder.com/stat?c=problem_statement&pm=13772

def possible( E, EM, M, MH, H, numSets ):
    # increment E to numSets
    EM -= (numSets-E)
    #increment H to numSets
    MH -= (numSets-H)
    if EM < 0 or MH < 0:
        return False
    return ( (M + EM + MH) >= numSets )

class ProblemSetsEasy(object):
    def maxSets(self, E, EM, M, MH, H):
        #foundSolution = 0
        ## linear search
        #for i in range(170000):
        #    if possible(E, EM, M, MH, H, i):
        #        foundSolution = i
        #return foundSolution

        # binary search is better
        lo = 0
        hi = 170000
        while lo < hi:
            mid = (lo + hi + 1)/2
            if possible(E, EM, M, MH, H, mid):
                lo = mid
            else:
                hi = mid-1
        assert lo == hi
        return lo

# test

cases = {
        (2,2,1,2,2):3,
        (100,100,100,0,0):0,
        (657,657,657,657,657):1095,
        (1,2,3,4,5):3,
        (100000,100000,100000,100000,100000):166666
        }

tester = ProblemSetsEasy()

for inp, exp in cases.iteritems():
    result = tester.maxSets( *inp )
    if result != exp:
        print "input: ", inp
        print "result: ", result
        print "expected: ", exp
        assert False


