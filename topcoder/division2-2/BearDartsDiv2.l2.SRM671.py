"""
https://community.topcoder.com/stat?c=problem_statement&pm=13479
        
Limak is an old brown bear who likes to play darts.

Limak just picked up an empty scorecard. He then threw a sequence of darts into a dartboard and for each dart he recorded the point value of the area it hit. You are given a int[] w containing the contents of Limak's scorecard: a sequence of point values.

Today there is a special jackpot. In order to win the jackpot, the player must present a scorecard with exactly four scores: (a, b, c, d). Additionally, these scores must be such that a*b*c = d. Note that order matters: the scores a, b, c, d must have been obtained in this particular order.

Limak wants to erase all but four scores from his scorecard in such a way that he will win the jackpot. Compute and return the number of different ways in which he can do that.
 
Definition
        
Class:  BearDartsDiv2
Method: count
Parameters: int[]
Returns:    long
Method signature:   long count(int[] w)
(be sure your method is public)
    
 
Notes
-   Pay attention to the unusual time limit.
 
Constraints
-   w will contain between 4 and 500 elements, inclusive.
-   Each element in w will be between 1 and 10^6, inclusive.

"""

from collections import Counter

class BearDartsDiv2:
    def count(self, scores):
        appearances = {}
        #appearances maps (number, index) -> count
        #which denotes how many times number appears after
        #index in scores
        seen = set()
        for i in range(len(scores)):
            if scores[i] in seen:
                continue
            else:
                seen.add(scores[i])
            count = 0
            for j in range(len(scores)-1, -1, -1):
                if scores[j] == scores[i] and j>=i:
                    count += 1
                appearances[(scores[i], j)] = count
        total = 0
        for i in range(len(scores)-3):
            for j in range(i+1, len(scores)-2):
                for k in range(j+1, len(scores)-1):
                    product = scores[i] * scores[j] * scores[k]
                    if (product, k+1) in appearances:
                        total += appearances[(product, k+1)]
        return total


 
cases = [        
        [[10,2,2,7,40,160],2],
        [[128,64,32,16,8,4,2,1],0],
        [[2,3,4,5,6,8,12,16,20,24,40,24,20,16,12,8,6,5,4,3,2],3],
        [[100,100,100,1000000,1000000,1000000,1000000,1000000],5],     
        [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],2573031125]
]

solution = BearDartsDiv2()
for inp, expectedOutput in cases:
    result = solution.count(inp)
    if result != expectedOutput:
        print "test failed"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expectedOutput
        assert False
print "All tests passed"

