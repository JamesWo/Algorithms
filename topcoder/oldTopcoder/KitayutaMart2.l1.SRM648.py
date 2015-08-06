#http://community.topcoder.com/stat?c=problem_statement&pm=13650

class KitayutaMart2(object):
    def numBought(self, k, t):
        total = 0
        multiplier = 1
        count = 0
        while total < t:
            total += multiplier * k
            multiplier *= 2
            count += 1
        assert total == t
        return count
        

# test

cases = {

(100,
100): 1,
        
(100,
300): 2,
        
(150,
1050): 3,
        
(160,
163680): 10,

}

tester = KitayutaMart2()

for inp, expected in cases.iteritems():
    result = tester.numBought(*inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False


