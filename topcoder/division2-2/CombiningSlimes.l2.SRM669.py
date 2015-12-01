"""
Problem Statement
        
The idols Ami and Mami like playing games. Today they bought a new game. At the beginning of the game a group of slimes appears on the screen. In each turn of the game the player can select any two of the slimes and merge them together. The game ends when there is only one slime left.

Each slime has a positive integer size. Whenever the player merges two slimes, the size of the merged slime is x+y, where x and y are the sizes of the two merged slimes. Additionally, the player is awarded x*y mascots for performing this merge.

Ami and Mami have just started a new game. You are given a int[] a containing the initial sizes of all slimes. Ami and Mami really like mascots. Find and return the maximum total number of mascots they can obtain during the game.

 
Definition
        
Class:  CombiningSlimes
Method: maxMascots
Parameters:     int[]
Returns:        int
Method signature:       int maxMascots(int[] a)
(be sure your method is public)
    
 
Constraints
-       a will contain between 2 and 100 elements, inclusive.
-       Each element of a will be between 1 and 100, inclusive.
 
"""

# the trick is that any permutation of combining slimes yields the same
# final score.  

class CombiningSlimes:
    def maxMascots(self, slimes):
        totalScore = 0
        totalSize = 0
        for slime in slimes:
            totalScore += (totalSize * slime)
            totalSize += slime
        return totalScore

# test
testCases = [
    [[3,4], 12],
    [[2,2,2], 12],
    [[1,2,3], 11],
    [[3,1,2], 11],
    [[7,6,5,3,4,6], 395]
]   

solution = CombiningSlimes()
for testInput, expectedOutput in testCases:
    result = solution.maxMascots(testInput)
    if result != expectedOutput:
        print "Test failed on input: %s, result: %s, expected: %s" % \
                (str(testInput), str(result), str(expectedOutput))
        assert False
print "Tests Passed"
