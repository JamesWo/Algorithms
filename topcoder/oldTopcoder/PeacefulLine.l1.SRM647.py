#http://community.topcoder.com/stat?c=problem_statement&pm=13632

class PeacefulLine(object):
    def makeLine(self, ages):
        counts = {}
        for age in ages:
            if age in counts:
                counts[age]+=1
            else:
                counts[age]=1
        maxAge = max(counts.itervalues())
        if maxAge <= ( len(ages)+1 )/2:
            return "possible"
        else:
            return "impossible"





# test

tester = PeacefulLine()

cases = {
 
(1,2,3,4): "possible",
        
(1,1,1,2): "impossible",
        
(1,1,2,2,3,3,4,4): "possible",
        
(3,3,3,3,13,13,13,13): "possible",
        
(3,7,7,7,3,7,7,7,3): "impossible",
        
(25,12,3,25,25,12,12,12,12,3,25): "possible",
        
(3,3,3,3,13,13,13,13,3): "possible",

}


for inp, expected in cases.iteritems():
    inp = list( inp )
    result = tester.makeLine(inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

