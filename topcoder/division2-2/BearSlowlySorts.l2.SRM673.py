"""
https://community.topcoder.com/stat?c=problem_statement&pm=14083

Limak is a little polar bear. He has a int[] w containing a sequence of N distinct numbers. He wants to sort this sequence into ascending order.

Limak knows some fast sorting algorithms but in the real world such knowledge sometimes isn't enough. In order to sort the sequence w Limak must physically move the numbers into their correct places. Such a thing can be hard for a little bear.

In a single move Limak can take all elements he can reach and sort them into ascending order. The problem is that Limak's arms are too short. Regardless of where he stands, he can only reach N-1 consecutive elements of w. Hence, in each move he can either sort all elements except for the last one, or all elements except for the first one.

Limak can make the moves in any order he likes. Compute and return the smallest number of moves necessary to sort the given sequence w.
 
Definition
        
Class:  BearSlowlySorts
Method: minMoves
Parameters: int[]    int
Method signature:   int minMoves(int[] w)
(be sure your method is public)
    
 
Constraints
-   w will contain between 3 and 50 elements, inclusive.
-   Each element in w will be between 1 and 1000, inclusive.
-   w will contain distinct elements.
 
"""

class BearSlowlySorts:
    def minMoves(self, lst):
        if sorted(lst) == lst:
            return 0
        if all(lst[0] <= x for x in lst) or all(lst[-1] >= x for x in lst):
            return 1
        if all(lst[0] > x for x in lst[1:]) and all(lst[-1] < x for x in lst[:-1]):
            return 3
        return 2

cases = [
    [[2,6,8,5], 1],
    [[4,3,1,6,2,5],2],
    [[93,155,178,205,213,242,299,307,455,470,514,549,581,617,677], 0],
    [[50,20,30,40,10], 3],
    [[234,462,715,596,906,231,278,223,767,925,9,526,369,319,241,354,317,880,5,696], 2]
]

solution = BearSlowlySorts()
for inp, expectedOutput in cases:
    result = solution.minMoves(inp)
    if result != expectedOutput:
        print "test failed"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expectedOutput
        assert False
        
