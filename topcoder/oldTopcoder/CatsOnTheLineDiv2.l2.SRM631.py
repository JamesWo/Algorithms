#http://community.topcoder.com/stat?c=problem_statement&pm=13392
"""
 Problem Statement for CatsOnTheLineDiv2

There are some cats sitting on a straight line that goes from the left to the right. You are given two int[]s position and count. For each valid i, there are count[i] cats initially sitting at the point position[i].

During each minute, each cat chooses and performs one of three possible actions: it may stay in its place, move one unit to the left (i.e., from x to x-1), or move one unit to the right (i.e., from x to x+1). (Note that there are no restrictions. In particular, different cats that are currently at the same point may make different choices.)

You are also given an int time. The goal is to rearrange the cats in such a way that each point contains at most one cat. Return "Possible" if it's possible to achive the goal in time minutes, and "Impossible" otherwise (quotes for clarity).

 
Definition
        
Class:  CatsOnTheLineDiv2
Method: getAnswer
Parameters:     int[], int[], int
Returns:        String
Method signature:       String getAnswer(int[] position, int[] count, int time)
(be sure your method is public)
    
 
Constraints
-       position will contain between 1 and 50 elements, inclusive.
-       position and count will contain the same number of elements.
-       Each element of position will be between -1000 and 1000, inclusive.
-       All elements of position will be distinct.
-       Each element of count will be between 1 and 1000, inclusive.
-       time will be between 0 and 1000, inclusive.
 
Examples
0)      
        
{0}
{7}
3
Returns: "Possible"
There are 7 cats sitting at the origin in this case. There are also 7 different points that cats can reach in 3 minutes, so each cat can occupy a unique point. Thus, the answer is "Possible".
1)      
        
{0}
{8}
2
Returns: "Impossible"
Unlike the first test case, in this case there are 8 cats for 7 available points. Thus, the answer is "Impossible".
2)      
        
{0, 1}
{3, 1}
0
Returns: "Impossible"
3)      
        
{5, 0, 2}
{2, 3, 5}
2
Returns: "Impossible"
4)      
        
{5, 1, -10, 7, 12, 2, 10, 20}
{3, 4, 2, 7, 1, 4, 3, 4}
6
Returns: "Possible"
"""


class CatsOnTheLineDiv2:
    def getAnswer(self, position, count, time):
        possible = [0] * 4001
        sortedPosCount = sorted( zip( position, count ), key=lambda x:x[0] )
        for pos, count in sortedPosCount:
            minPos = pos - time
            maxPos = pos + time
            index = minPos
            while count > 0:
                if index > maxPos:
                    return "Impossible"
                if possible[index] == 0:
                    possible[index] = 1
                    index += 1
                    count -= 1
                else:
                    index += 1
        return "Possible"

tester = CatsOnTheLineDiv2()

cases = {
        
((0,), (7,), 3): "Possible",
((0,), (8,), 2): "Impossible",
((0, 1,), (3, 1,), 0): "Impossible",
((5, 0, 2,), (2, 3, 5,), 2): "Impossible",
((5, 1, -10, 7, 12, 2, 10, 20,), (3, 4, 2, 7, 1, 4, 3, 4,), 6): "Possible",

}


for inp, expected in cases.iteritems():
    position = list(inp[0])
    count = list(inp[1])
    time = inp[2]
    result = tester.getAnswer(position, count, time)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

