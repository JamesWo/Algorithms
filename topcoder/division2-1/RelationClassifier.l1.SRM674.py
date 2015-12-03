"""
https://community.topcoder.com/stat?c=problem_statement&pm=14008
        
Weiwei is studying math. Unfortunately, math is very hard for him. Today, the teacher asked Weiwei to determine if a relation is a bijection or not.

Formally, a relation is a set of ordered pairs of elements. The teacher gave Weiwei one such relation. You are also given a description of this relation: int[]s domain and range. For each valid i, the relation contains the ordered pair (domain[i], range[i]).

Let X be the set of elements that appear at least once in domain. Similarly, let Y be the set of elements that appear at least once in range. We say that an element x of X is paired to an element y of Y if the relation contains the ordered pair (x, y).

We will say that our relation is a bijection if each element of X is paired to exactly one element of Y, and each element of Y is paired to exactly one element of X.

If Weiwei's relation is a bijection, return "Bijection" (quotes for clarity). Otherwise, return "Not". Note that the return value is case-sensitive.

 
Definition
        
Class:  RelationClassifier
Method: isBijection
Parameters:     int[], int[]
Returns:        String
Method signature:       String isBijection(int[] domain, int[] range)
(be sure your method is public)
    
 
Constraints
-       domain will contain between 1 and 10 elements, inclusive.
-       range will contain the same number of elements as domain.
-       Each element of domain and range will be between 1 and 100, inclusive.
-       No two pairs (domain[i], range[i]) will be identical.
 
"""

class RelationClassifier:
    def isBijection(self, X, Y):
        xmapping = {}
        ymapping = {}  
        for i in range(len(X)):
            if X[i] in xmapping and xmapping[X[i]] != Y[i]:
                return "Not"
            if Y[i] in ymapping and ymapping[Y[i]] != X[i]:
                return "Not"
            xmapping[X[i]] = Y[i]
            ymapping[Y[i]] = X[i]
        return "Bijection"

tester = RelationClassifier()

cases = [
        [[1,1],[2,3],"Not"],
        [[4,5],[2,2],"Not"],
        [[1,2,3,4,5],[1,2,3,4,5],"Bijection"],
        [[14, 12, 10, 13, 20, 18, 9, 17, 14, 9],
            [18, 6, 8, 15, 2, 14, 10, 13, 13, 15],
            "Not"]
        ]

for X, Y, expectedOutput in cases:
    result = tester.isBijection(X, Y)
    if result != expectedOutput:
        print "Test case failed"
        print "Input: ", X, Y
        print "output: ", result
        print "expected: ", expectedOutput
        assert False

print "tests passed"
