# http://community.topcoder.com/stat?c=problem_statement&pm=13463

"""
 Problem Statement for Jumping
Problem Statement
        Frog Suwako lives on a two-dimensional plane. She likes to jump. Currently, she is located in the point (0, 0). She would like to reach the point (x, y). You are given the ints x and y. 

Suwako wants to reach the desired destination in a specific way: using a series of jumps with pre-determined lengths. You are given these lengths in a int[] jumpLenghts. For example, if jumpLengths = { 2, 5 }, Suwako must make a jump of length exactly 2, followed by a jump of length exactly 5. 

Note that Suwako can jump onto arbitrary points in the plane, they are not required to have integer coordinates. Return "Able" (quotes for clarity) if Suwako is able to reach her desired destination from (0, 0) using the desired sequence of jump lengths. Otherwise, return "Not able".
 
Definition
        
Class:  Jumping
Method: ableToGet
Parameters:     int, int, int[]
Returns:        String
Method signature:       String ableToGet(int x, int y, int[] jumpLengths)
(be sure your method is public)
    
 
Constraints
-       x will be between -1,000 and 1,000, inclusive.
-       y will be between -1,000 and 1,000, inclusive.
-       len will contain between 1 and 50 elements, inclusive.
-       Each element in len will be between 1 and 1,000, inclusive.
 
Examples
0)      
        
5
4
{2, 5}
Returns: "Able"
One possibility is to jump from (0, 0) to (2, 0), and then from (2, 0) to (5, 4).
1)      
        
3
4
{4}
Returns: "Not able"
The distance from (0, 0) to (3, 4) is 5. You cannot get there using a single jump of length 4 - it is too short.
2)      
        
3
4
{6}
Returns: "Not able"
The distance from (0, 0) to (3, 4) is 5. You cannot get there using a single jump of length 6 - it is too long.
3)      
        
0
1
{100, 100}
Returns: "Able"
Here, one possible solution looks as follows: Let t = sqrt(100*100 - 0.5*0.5). Suwoko will make her first jump from (0, 0) to (t, 0.5), and her second jump from (t, 0.5) to (0, 1).
4)      
        
300
400
{500}
Returns: "Able"
5)      
        
11
12
{1,2,3,4,5,6,7,8,9,10}
Returns: "Able"
6)      
        
11
12
{1,2,3,4,5,6,7,8,9,100}
Returns: "Not able"

"""
import math

# TODO This may be buggy, test more later

class Jumping:
    def ableToGet(self, x, y, jumpLengths):
        goalDist = math.sqrt( x**2 + y**2 )
        maxIndex = jumpLengths.index( max( jumpLengths ) )
        rest = sum( jumpLengths[ :maxIndex ] + jumpLengths[ maxIndex+1: ] )
        lo = jumpLengths[ maxIndex ] - rest
        hi = jumpLengths[ maxIndex ] + rest
        if goalDist >= lo and goalDist <= hi:
            return "Able"
        else:
            return "Not able"

cases = {
(5, 4, (2, 5)): "Able",
(3, 4, (4,)): "Not able",
(3, 4, (6,)): "Not able",
(0, 1, (100, 100)): "Able",
(300, 400, (500,)): "Able",
(11, 12, (1,2,3,4,5,6,7,8,9,10)): "Able",
(11, 12, (1,2,3,4,5,6,7,8,9,100)): "Not able",
}

tester = Jumping()


for inp, expected in cases.iteritems():
    x = inp[0]
    y = inp[1]
    j = list(inp[2])
    result = tester.ableToGet(x, y, j)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False


