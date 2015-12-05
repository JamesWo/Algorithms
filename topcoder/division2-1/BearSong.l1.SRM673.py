"""
https://community.topcoder.com/stat?c=problem_statement&pm=14082

Bear Limak has recently learned about musical notes. He then listened to a song and noticed that some notes appeared less often than others. In fact, some notes were so rare that they appeared in the song only once!

Limak now wants to look for such notes in other songs. Write a program that will look for the rare notes.

You are given a int[] notes that describes a song. Each number in notes represents one note of the song. Different numbers represent different notes, equal numbers represent equal notes.

Compute and return the number of notes that occur exactly once in the given song.
 
Definition
        
Class:  BearSong
Method: countRareNotes
Parameters: int[]
Returns:    int
Method signature:   int countRareNotes(int[] notes)
(be sure your method is public)
    
 

Constraints
-   notes will contain between 1 and 50 elements, inclusive.
-   Each element in notes will be between 1 and 1000, inclusive.
"""


from collections import Counter

class BearSong:
    def countRareNotes(self, notes):
        return Counter(notes).values().count(1)


cases =  [        
    [[9,10,7,8,9],3],
    [[8,8,7,6,7,3,5,10,9,3],4],
    [[234,462,715,596,906],5],
    [[17],1],
    [[1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,
    1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,
    1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],0]
]

solution = BearSong()
for inp, expectedOutput in cases:
    result = solution.countRareNotes(inp)
    if result != expectedOutput:
        print "Test failed"
        print "input: ", inp
        print "result: ", result
        print "expected: ", expectedOutput
        assert False
