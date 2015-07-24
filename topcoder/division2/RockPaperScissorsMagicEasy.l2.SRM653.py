# http://community.topcoder.com/stat?c=problem_statement&pm=13686

class RockPaperScissorsMagicEasy(object):
    def count( self, card, score ):
        return -1



# test

cases = {
        ((0, 1, 2), 2):6,
        ((1, 2), 0):4,
        ((2,2,1,0,0),10):0,
        ((0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2),7):286226628,
        ((0,1,2,0,1,2,2,1,0),8):18,
    }

tester = RockPaperScissorsMagicEasy()

for inp, expected in cases.iteritems():
    result = tester.count( list(inp[0]), inp[1] )
    if result != expected:
        print "inp ",inp
        print "result ",result
        print "expected ",expected
        assert False
