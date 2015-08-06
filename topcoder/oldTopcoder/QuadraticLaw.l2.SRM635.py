#http://community.topcoder.com/stat?c=problem_statement&pm=13486
"""
 Problem Statement for QuadraticLaw
        
"N?mec's quadratic law: how many minutes the teacher was late to the lesson, that many minutes squared he'll end the lesson earlier."

In other words, if the teacher is t minutes late (for some non-negative integer t), he should end the lesson t2 minutes early. Of course, this means the teacher can't be too late, because a lesson can't end before even starting. It is, however, possible for the teacher to arrive and end the lesson immediately (in fact, he then only arrives to tell the students that the lesson's cancelled).

You're given a long d. The lesson was supposed to take d minutes. Compute and return the largest non-negative integer t such that the teacher can be t minutes late.

Definition
        
Class:  QuadraticLaw
Method: getTime
Parameters:     long
Returns:        long
Method signature:       long getTime(long d)
(be sure your method is public)
    
 
Constraints
-       d will be between 1 and 1,000,000,000,000,000,000, inclusive.
 
Examples
0)      
        
1
Returns: 0
The lesson was supposed to take 1 minute. The teacher can only be 0 minutes late, in which case he ends the lesson 0 minutes early (i.e. he arrives and ends the lecture on time).
1)      
        
2
Returns: 1
It's possible for the teacher to be 1 minute late and end the lecture 1 minute early (so there's no lecture at all).
2)      
        
5
Returns: 1
3)      
        
6
Returns: 2
4)      
        
7
Returns: 2
5)      
        
1482
Returns: 38
6)      
        
1000000000000000000
Returns: 999999999
7)      
        
31958809614643170
Returns: 178770270

"""

MIN = 1
MAX = 1000000000000000000
class QuadraticLaw:
    def getTime(self, d):
        if d <= 1:
            return 0
        # binary search for the highest x such that x(x+1) <= d
        lo = MIN
        hi = MAX
        while lo < hi:
            mid = ( lo + hi + 1) / 2
            if (mid*(mid+1)) <= d:
                lo = mid
            else:
                hi = mid - 1
        return lo


tester = QuadraticLaw()

cases = {
        1:0,
        2:1,
        5:1,
        6:2,
        7:2,
        1482:38,   
        1000000000000000000: 999999999,
        31958809614643170: 178770270,
}

for inp, expected in cases.iteritems():
    result = tester.getTime(inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

