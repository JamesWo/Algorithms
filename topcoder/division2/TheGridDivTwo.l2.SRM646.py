#http://community.topcoder.com/stat?c=problem_statement&pm=13628
"""
 Problem Statement for TheGridDivTwo


Problem Statement
        John is standing at the origin of an infinite two-dimensional grid. He is going to move along this grid. During each second he can either stay where he is or he can move by one unit in one of the four cardinal directions (north, south, east, or west). Some of the grid points are blocked. John is not allowed to move to a blocked grid point. 



You are given the coordinates of the blocked grid points as int[]s x and y. For each valid i, the grid point that is x[i] units east and y[i] units north of the origin is blocked. You are also given an int k. Compute and return the maximal possible x-coordinate of a point John can reach in k seconds.
 
Definition
        
Class:  TheGridDivTwo
Method: find
Parameters:     int[], int[], int
Returns:        int
Method signature:       int find(int[] x, int[] y, int k)
(be sure your method is public)
    
 
Constraints
-       x will contain between 0 and 47 elements, inclusive.
-       x and y will contain the same number of elements.
-       Each element of x will be between -1,000 and 1,000, inclusive.
-       Each element of y will be between -1,000 and 1,000, inclusive.
-       All pairs (x[i], y[i]) will be distinct.
-       Each pair (x[i], y[i]) will be different from (0, 0).
-       k will be between 1 and 1,000, inclusive.
 
Examples
0)      
        
{1,1,1,1}
{-2,-1,0,1}
4
Returns: 2
The optimal strategy is to move two times north to (0, 2) and then two times east to (2,2).
1)      
        
{-1, 0, 0, 1}
{0, -1, 1, 0}
9
Returns: 0
John can not make any moves.
2)      
        
{}
{}
1000
Returns: 1000
3)      
        
{1,0,0,-1,-1,-2,-2,-3,-3,-4,-4}
{0,-1,1,-2,2,-3,3,-4,4,-5,5}
47
Returns: 31
"""

from Queue import Queue
from collections import deque

class TheGridDivTwo(object):
    seen = set()
    invalid = set()
    Q = Queue()
    bestX = None

    def find1(self, x, y, k):
        self.seen = set()
        self.invalid = set()
        self.Q = Queue()
        self.bestX = 0
        # hash each invalid position
        for i in range(len(x)):
            self.invalid.add((x[i], y[i]))

        # dbfs for the highest y position reachable
        self.Q.put( (0, 0, k) )
        while not self.Q.empty():
            x, y, ttl = self.Q.get_nowait()
            self.bestX = max(self.bestX, x)
            if ttl == 0:
                continue 
            for newPos in ( (x, y-1), (x, y+1), (x-1, y), (x+1, y) ):
                if newPos in self.seen:
                    continue
                if newPos in self.invalid:
                    continue
                else:
                    self.seen.add(newPos)
                    self.Q.put( ( newPos[0], newPos[1], ttl-1 ) )
        return self.bestX            

    # same as find1, but does not use python Queue.Queue
    def find2(self, x, y, k):
        self.seen = set()
        self.invalid = set()
        self.Q = deque()
        self.bestX = 0
        # hash each invalid position
        for i in range(len(x)):
            self.invalid.add((x[i], y[i]))

        self.Q.append( (0, 0, k) ) #appends to right of deque
        while len(self.Q) != 0:
            x, y, ttl = self.Q.popleft()
            self.bestX = max(self.bestX, x)
            if ttl == 0:
                continue 
            for newPos in ( (x, y-1), (x, y+1), (x-1, y), (x+1, y) ):
                if newPos in self.seen or newPos in self.invalid:
                    continue
                else:
                    self.seen.add(newPos)
                    self.Q.append( ( newPos[0], newPos[1], ttl-1 ) )
        return self.bestX            


    # same as find1/2, but uses a huge list instead of a Queue
    def find3(self, x, y, k):
        self.seen = set()
        self.invalid = set()

        Q = [ 0 ] * (((2*k+1)**2)+1)
        Qstart = 0
        Qend = 0

        self.bestX = 0
        # hash each invalid position
        for i in range(len(x)):
            self.invalid.add((x[i], y[i]))

        Q[Qend] = ( (0, 0, k) )
        Qend += 1
        while Qstart < Qend:
            x, y, ttl = Q[Qstart]
            Qstart += 1
            self.bestX = max(self.bestX, x)
            if ttl == 0:
                continue 
            for newPos in ( (x, y-1), (x, y+1), (x-1, y), (x+1, y) ):
                if newPos in self.seen or newPos in self.invalid:
                    continue
                else:
                    self.seen.add(newPos)
                    Q[Qend] = ( ( newPos[0], newPos[1], ttl-1 ) )
                    Qend += 1
        return self.bestX            



    def find(self, x, y, k):
        return self.find2(x, y, k)




# test

cases = {
  
((1,1,1,1),
(-2,-1,0,1),
4): 2,

((-1, 0, 0, 1),
(0, -1, 1, 0),
9): 0,
        
((),
(),
1000): 1000,
        
((1,0,0,-1,-1,-2,-2,-3,-3,-4,-4),
(0,-1,1,-2,2,-3,3,-4,4,-5,5),
47): 31,

}

tester = TheGridDivTwo() 

for inp, expected in cases.iteritems():
    x = list( inp[0] )
    y = list( inp[1] )
    k = inp[2]
    result = tester.find(x, y, k)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False


