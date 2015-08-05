#http://community.topcoder.com/stat?c=problem_statement&pm=13524
"""
 Problem Statement for AliceGameEasy
        
Alice and Kirito just played a game. The game consisted of a finite (possibly empty) sequence of turns. You do not know the exact number of turns. The turns were numbered starting from 1. In each turn, exactly one of our two players won. The winner of turn i scored i points.

You are given two longs x and y. Find out whether it is possible that at the end of the game Alice had exactly x points and Kirito had exactly y points. If it is possible, return the smallest number of turns Alice could have won. If the given final result is not possible, return -1 instead.

 
Definition
        
Class:  AliceGameEasy
Method: findMinimumValue
Parameters:     long, long
Returns:        long
Method signature:       long findMinimumValue(long x, long y)
(be sure your method is public)
    
 
Constraints
-       x and y will be between 0 and 1,000,000,000,000(10^12), inclusive.
 
Examples
0)      
        
7
14
Returns: 2
This final result is possible. One possibility is that Alice won turns 1, 2, and 4 (for 1+2+4 = 7 points) and Kirito won turns 3, 5, and 6 (for 3+5+6 = 14 points). However, there are also some other possibilities in which Alice only won two of the six turns, so the correct answer is 2.
1)      
        
10
0
Returns: 4
There must have been four turns and Alice must have won all four of them.
2)      
        
932599670050
67400241741
Returns: 1047062
Watch out for integer overflow.
3)      
        
7
13
Returns: -1
4)      
        
0
0
Returns: 0
5)      
        
100000
400500
Returns: 106


"""

class AliceGameEasy:
    def findMinimumValue(self, x, y):
        # figure out how many games were played
        total = 0
        gameNum = 1
        while total < x + y:
            total += gameNum
            gameNum += 1
        if total > x + y:
            return -1
        gameNum -= 1
        # calculate minimum number of games alice won
        # the optimal solution has alice winning the highest-valued games
        count = 0
        while x > gameNum:
            count += 1
            x -= gameNum
            gameNum -= 1
        if x > 0:
            count += 1
        return count


tester = AliceGameEasy()

cases = {

(7, 14):2,
(10, 0): 4,
(932599670050, 67400241741): 1047062,
(7, 13): -1,
(0, 0):0,
(100000, 400500): 106,

}

for inp, expected in cases.iteritems():
    result = tester.findMinimumValue(*inp)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

