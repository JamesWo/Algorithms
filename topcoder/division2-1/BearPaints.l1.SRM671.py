"""
https://community.topcoder.com/stat?c=problem_statement&pm=13488

Limak is a little polar bear. Today he found two things in the snow: a bucket of blue paint and a white rectangular grid with W times H square cells.

Limak is going to paint some (possibly even all) cells blue. He wants to do it in such a way that the blue cells will form a completely filled blue rectangle. He has enough paint for M cells. What is the largest possible area of a blue rectangle he can paint?

 
Definition
        
Class:  BearPaints
Method: maxArea
Parameters:     int, int, long
Returns:        long
Method signature:       long maxArea(int W, int H, long M)
(be sure your method is public)
    
 
Constraints
-       W and H will be between 1 and 10^6, inclusive.
-       M will be between 1 and 10^12, inclusive.
 
"""


class BearPaints:
    def maxArea(self, width, height, paint):
        bestArea = 0
        for w in range(1,width+1):
            h = min(height, paint/w)
            bestArea = max(bestArea, h*w)
        return bestArea


# test            

cases = [
        [[3,5,14], 12],
        [[4,4,10],9],
        [[1000000,12345,1000000000000],12345000000],
        [[1000000,1000000,720000000007],720000000000],
        [[1000000,1000000,999999999999],999999000000]]

tester = BearPaints()
for inp, expectedOutput in cases:
    result = tester.maxArea(*inp)
    if result != expectedOutput:
        print "test failed"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expectedOutput
        assert False

print "tests passed"
