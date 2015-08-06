#http://community.topcoder.com/stat?c=problem_statement&pm=13698

class OneEntrance(object):
    def count(self, a, b, s):
        return -1









# test

tester = OneEntrance()

cases = {
        
(
    (0, 1, 2),
    (1, 2, 3),
    0
):1,

(
    (0, 1, 2),
    (1, 2, 3),
    2,
):3,

(
    (0, 0, 0, 0),
    (1, 2, 3, 4),
    0,
):24,

(
    (7, 4, 1, 0, 1, 1, 6, 0),
    (6, 6, 2, 5, 0, 3, 8, 4),
    4,
):896,

(
    (),
    (),
    0,
):1,

}

for inp, expected in cases.iteritems():
    result = tester.count( list(inp[0]), list(inp[1]), inp[2] )
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False
