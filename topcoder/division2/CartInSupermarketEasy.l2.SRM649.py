#http://community.topcoder.com/stat?c=problem_statement&pm=13659

class CartInSupermarketEasy:
    def calc(self, N, K):


# test

tester = CartInSupermarketEasy()

cases = {
        #(5,0):5,
        #(5,2):4,
        (15,4):6,
        #(7,100):4,
        #(45,5):11,
        #(100,100):8,
        }

for inp, expected in cases.iteritems():
    result = tester.calc(*inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        import pdb; pdb.set_trace()
        assert False
