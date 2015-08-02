# http://community.topcoder.com/stat?c=problem_statement&pm=13721
"""
 Problem Statement for FoldingPaper2
        
You have a rectangular piece of paper. Its dimensions are W times H. You want to have a paper with area A instead. Therefore, you decided to fold the paper you have. In each step you can fold the paper according to a straight line. There are two restrictions: First, that line must always be parallel to one of the rectangle's sides. Second, after each fold both dimensions of the new rectangle must be integers again.

For example, suppose that your paper is 5 units wide and 3 units tall. If you fold it according to a vertical line that is 4 units to the right of its left side, you will obtain a rectangle that is 4 units wide and 3 units tall. If you fold it according to a horizontal line that is 1 unit below the top of the rectangle, you will get a rectangle that is 5 units wide and 2 units tall.

You are given the ints W, H, and A. If it is impossible to fold the paper into a valid rectangle with area A, return -1. Otherwise, return the smallest number of times you need to fold the paper.

 
Definition
        
Class:  FoldingPaper2
Method: solve
Parameters:     int, int, int
Returns:        int
Method signature:       int solve(int W, int H, int A)
(be sure your method is public)
    
 
Constraints
-       H, W will be between 1 and 1,000,000,000, inclusive.
-       A will be between 1 and 100,000, inclusive.
 

"""
import math

class FoldingPaper2(object):
    def getNumFolds(self, initial, end):
        """
        returns the number of folds required to convert initial to end
        """
        cost = 0
        if initial < end:
            return float('inf')
        while initial > end:
            # fold initial in half.  
            # don't worry if we go pass end, since we just care about
            # the number of folds required
            # round up
            initial = (initial+1)/2
            cost += 1
        return cost

    def solve(self, W, H, A):
        best = float('inf')
        # find all possible integers (x, y) such that x * y = A
        # we only need to try up square root of A
        for i in range(1, int(math.sqrt(A))+1):
            if A % i != 0:
                continue
            j = A / i
            # try folding both ways ( W to i, H to j, or W to j, H to i )
            # number of folds in each direction is orthogonal to the orthogonal direction
            cost1 = self.getNumFolds(W, i) + self.getNumFolds(H, j)
            cost2 = self.getNumFolds(W, j) + self.getNumFolds(H, i)
            best = min(best, cost1, cost2)
        if best == float('inf'):
            return -1
        return best




cases = {

(5,
3,
12): 1,
        
(2,
2,
3): -1,
        
(4,
4,
1): 4,
        
(127,
129,
72,): 8,
        
(1,
100000,
100000,): 0,
        
(1,
1,
2,): -1,

}

tester = FoldingPaper2()

for inp, expected in cases.iteritems():
    result = tester.solve(*inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

