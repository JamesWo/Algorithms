#http://community.topcoder.com/stat?c=problem_statement&pm=13679

def gcd(a, b):
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

def lcm(a, b):
    return (a*b)/gcd(a,b)

def lcmList( lst ):
    return reduce(lcm, lst)

class ThePermutationGameDiv2:
    def findMin(self, N):
        return lcmList(range(1, N+1))

# test

cases = {
        2:2,
        3:6,
        6:60,
        11:27720,
        25:26771144400,
}

tester = ThePermutationGameDiv2()

for case, out in cases.iteritems():
    result = tester.findMin(case)
    if result != out:
        print "Failed test, input = %s" % str(case)
        print "output = %s" % result
        print "expected = %s" % out
        assert False


