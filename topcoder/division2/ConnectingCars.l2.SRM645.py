#http://community.topcoder.com/stat?c=problem_statement&pm=13602
"""
Problem Statement for ConnectingCars
        
Janusz works in roller coaster maintenance. The station of the roller coaster is a long straight segment of railroad tracks. There are some cars on those tracks. The cars are currently not attached to each other, and there may be gaps between some of them. Janusz has to push them all together and connect them into a train.

You are given the int[]s positions and lengths. For each valid i, there is a car that is lengths[i] meters long and starts positions[i] meters from the beginning of the station. (In other words, the coordinates currently occupied by this car are in the interval from positions[i] to positions[i]+lengths[i].)

Moving a single car one meter in either direction costs Janusz one unit of energy. Compute the smallest total amount of energy sufficient to push all cars together. In the final configuration the cars must be located one after another with no gaps between them.

(Note that there is no restriction on the movement of cars or on the final position of the train. Janusz may push the cars in any order, and he may even push some cars by a non-integer number of meters if he wants to.)

 
Definition
        
Class:  ConnectingCars
Method: minimizeCost
Parameters:     int[], int[]
Returns:        long
Method signature:       long minimizeCost(int[] positions, int[] lengths)
(be sure your method is public)
    
 
Notes
-       You may assume that the optimal answer is always an integer that fits into a signed 64-bit integer data type.
 
Constraints
-       lengths and positions will have the same number of elements.
-       lengths will have between 2 and 50 elements, inclusive.
-       Each element of lengths and positions will be between 1 and 10^9, inclusive.
-       The segments occupied by the cars may touch but they will not overlap.
 
"""

"""
analysis:
claim:
    In any optimal solution, at least one car does not move.
proof:
    Assume towards contradiction that in the optimal solution,
     all cars moved.  Since the final position of the cars are 
    connected back-to-back, there must be a pair of cars that
    moved towards eachother, in opposite directions (i.e.
    the left one moved right, and the right one moved left).  
    Let L be the left car in this pair, and R be the right car.
    Let X be the set of cars to the left of this pair (including
    the left car of the pair) and Y be the set of cars to 
    the right.  Then without loss of generality assume
    size(X) <= size(Y).  Then we would have a better solution
    if we did not move R, and instead move every element from X
    to the right until they connected to R.  Thus, the original
    solution was not optimal.
algorithm:
    Try each car, keeping it in the original position, and moving
    all other cars towards it.
"""
class ConnectingCars(object):
    def minimizeCost(self, positions, lengths):
        
        return 1














# test

cases = {

        
((1, 3, 10, 20),
(2, 2, 5, 3)): 15,
        
((100, 50, 1),
(10, 2, 1)): 96,
        
((4, 10, 100, 13, 80),
(5, 3, 42, 40, 9)): 66,
        
((5606451, 63581020, 81615191, 190991272, 352848147, 413795385, 468408016, 615921162, 760622952, 791438427),
(42643329, 9909484, 58137134, 99547272, 39849232, 15146704, 144630245, 604149, 15591965, 107856540)): 1009957100,


}


tester = ConnectingCars()


for inp, expected in cases.iteritems():
    positions = list( inp[0] )
    lengths = list( inp[1] )
    result = tester.minimizeCost(positions, lengths)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

