# http://community.topcoder.com/stat?c=problem_statement&pm=13520

"""

 Problem Statement for NarrowPassage2Easy
        
There is a narrow passage. Inside the passage there are some wolves. You are given a int[] size that contains the sizes of those wolves, from left to right. 

The passage is so narrow that some pairs of wolves cannot pass by each other. More precisely, two adjacent wolves may swap places if and only if the sum of their sizes is maxSizeSum or less. Assuming that no wolves leave the passage, what is the number of different permutations of wolves in the passage? Note that two wolves are considered different even if they have the same size. 

Compute and return the number of permutations of wolves that can be obtained from their initial order by swapping a pair of wolves zero or more times.
 
Definition
        
Class:  NarrowPassage2Easy
Method: count
Parameters:     int[], int
Returns:        int
Method signature:       int count(int[] size, int maxSizeSum)
(be sure your method is public)
    
 
Constraints
-       size will contain between 1 and 6 elements, inclusive.
-       Each element in size will be between 1 and 1,000, inclusive.
-       maxSizeSum will be between 1 and 1,000, inclusive.
 
Examples
0)      
        
{1, 2, 3}
3
Returns: 2
From {1, 2, 3}, you can swap 1 and 2 to get {2, 1, 3}. But you can't get other permutations.
1)      
        
{1, 2, 3}
1000
Returns: 6
Here you can swap any two adjacent wolves. Thus, all 3! = 6 permutations are possible.
2)      
        
{1, 2, 3}
4
Returns: 3
You can get {1, 2, 3}, {2, 1, 3} and {2, 3, 1}.
3)      
        
{1,1,1,1,1,1}
2
Returns: 720
All of these wolves are different, even though their sizes are the same. Thus, there are 6! different permutations possible.
4)      
        
{2,4,6,1,3,5}
8
Returns: 60
5)      
        
{1000}
1000
Returns: 1



"""
def canSwap(size, i, j, maxSizeSum):
    for wolf in range(j-1, i-1, -1):
        if size[j] + size[wolf] > maxSizeSum:
            return False
    return True

class NarrowPassage2Easy:
    def count(self, size, maxSizeSum):
        if len(size) == 1:
            return 1
        total = 0
        for i in range(len(size)):
            if canSwap(size, 0, i, maxSizeSum):
                total += self.count( size[:i] + size[i+1:], maxSizeSum )
        return total

tester = NarrowPassage2Easy()

cases = {
((1, 2, 3), 3): 2,
((1, 2, 3), 1000): 6,
((1, 2, 3), 4): 3,
((1,1,1,1,1,1), 2): 720,
((2,4,6,1,3,5), 8): 60,
((1000,), 1000): 1,
}

for inp, expected in cases.iteritems():
    size = list(inp[0])
    m = inp[1]
    result = tester.count(size, m)
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

