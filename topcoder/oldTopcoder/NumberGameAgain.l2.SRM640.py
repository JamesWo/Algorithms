#http://community.topcoder.com/stat?c=problem_statement&pm=13557

class NumberGameAgain(object):
    def solve(self, k, table):
        m = 2**k - 1
        intervals = []
        for i in table:
            add = 1
            while i <= m:
                intervals.append( (i, "open") )
                intervals.append( (i + add - 1, "close" ) )
                i *= 2
                add *= 2
        if not intervals:
            return m - 1
        # sort intervals
        intervals.sort( key = lambda x: x[1] )
        intervals.reverse()
        intervals.sort( key = lambda x: x[0] )
        
        # count closed 
        numClosed = 0
        prevOpen = intervals[ 0 ][ 0 ]
        opened = 1
        assert intervals[ 0 ][ 1 ] == 'open'
        for item in intervals[ 1: ]:
            if item[ 0 ] > m:
                if opened > 0:
                    numClosed += ( m - prevOpen + 1 )
                break
            if item[ 1 ] == 'open':
                if opened == 0:
                    prevOpen = item[ 0 ]
                opened += 1
            elif item[ 1 ] == 'close':
                opened -= 1
                if opened == 0:
                    numClosed += ( item[0] - prevOpen + 1)
        return m - 1 - numClosed



tester = NumberGameAgain() 

cases = {

(3, (2,4,6)) : 2,
(5, (2,3)): 0,
(5, ()):30,
(40, (2,4,8,16,32141531,2324577,1099511627775,2222222222,33333333333,4444444444,2135) ): 549755748288,
(40, ()): 1099511627774

}

for inp, expected in cases.iteritems():
    k = inp[0]
    table = list(inp[1])
    result = tester.solve(k, table)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

