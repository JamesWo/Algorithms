# PublicTransit
# http://community.topcoder.com/stat?c=problem_statement&pm=13793

import itertools
def manDist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def minDistWithTeleporterFixedPoint(x1, y1, x2, y2, start1, start2, end1, end2):
    """Returns the cost of best path from (start1, start2) to (end1, end2), given
    that a teleporter is placed at (x1,y1) and at (x2, y2).
    """
    c1 = manDist(start1, start2, end1, end2)
    c2 = manDist(start1, start2, x1, y1) + manDist(x2, y2, end1, end2)
    c3 = manDist(start1, start2, x2, y2) + manDist(x1, y1, end1, end2)
    return min(c1, c2, c3)

def allPairPos(rows, cols):
    allPos = tuple(itertools.product(range(rows), range(cols)))
    return itertools.product(allPos, allPos)

def maxDistWithTeleporter(rows, cols, x1, y1, x2, y2):
    """Returns the maximum distance between any two positions, given a teleporter.
    """
    best = 0
    for startPos, endPos in allPairPos(rows, cols):
        cost = minDistWithTeleporterFixedPoint(x1, y1, x2, y1, startPos[0], startPos[1], endPos[0], endPos[1] )
        best = max(best, cost)
    return best


class PublicTransit(object):
    def minimumLongestDistance(self, rows, cols):
        best = float("inf")
        for pos1, pos2 in allPairPos(rows, cols):
            newResult = maxDistWithTeleporter(rows, cols, pos1[0], pos1[1], pos2[0], pos2[1])
            best = min(best, newResult)
        return best

# test
cases = {
        (4,1):1,
        (2,2):1,
        (5,3):4,
        (8,2):4,
        }


tester = PublicTransit()

for inp, expected in cases.iteritems():
    result = tester.minimumLongestDistance(*inp)
    if (isinstance(expected, list) and result not in expected) or\
            (not isinstance(expected, list) and result != expected ):
        print "Failed:"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expected
        import pdb;pdb.set_trace()
        assert False
