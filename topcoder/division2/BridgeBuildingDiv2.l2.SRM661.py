# http://community.topcoder.com/stat?c=problem_statement&pm=13546

class BridgeBuildingDiv2(object):
    def minDiameter(self, a, b, k):
        return 0

tester = BridgeBuildingDiv2()

cases = {
        ((2,1,1,1,2), (1,9,1,9,1), 4): 6,
        
        ((1,50,1,50,1,50,1,50), (50,1,50,1,50,1,50,1), 9) : 8,
        
        ((50,10,15,31,20,23,7,48,5,50), (2,5,1,8,3,2,16,11,9,1), 3) : 124,
        
        ((2,4,10,2,2,22,30,7,28), (5,26,1,2,6,2,16,3,15), 5) : 54,

        }

for case, out in cases.iteritems():
    result = tester.minDiameter(list(case[0]), list(case[1]), case[2])
    if result != out:
        print "Failed test, input = %s" % str(case)
        print "output = %s" % result
        print "expected = %s" % out
