"""
https://community.topcoder.com/stat?c=problem_statement&pm=13948
        
Today, a large live concert is going to take place. Some interprets (called "idols") are going to perform at the concert. Different idols have different names.

There are M distinct songs that can be included in the concert. The songs are numbered 0 through M-1. Song i can only be performed by the idol s[i]. Including this song in the concert will increase the happiness of the audience by h[i].

We have to choose the set list for this concert. Our goal is to make the audience as happy as possible. However, the concert time is limited and therefore each idol can only perform at most one song.

You are given the int[] h and the String[] s with M elements each. Find the set of songs that should be played at the concert. The set of songs must have the following properties:

Each idol will perform at most one song.
After hearing the songs, the happiness of the audience will increase by the largest amount possible.
Return the largest possible amount of happiness the audience can gain.
 
Definition
        
Class:  LiveConcert
Method: maxHappiness
Parameters: int[], String[]
Returns:    int
Method signature:   int maxHappiness(int[] h, String[] s)
(be sure your method is public)
    
 
Notes
-   The value M is not given explicitly. You can determine M as the length of h.
 
Constraints
-   M will be between 1 and 100, inclusive.
-   h and s will contain exactly M elements each.
-   All numbers in h will be between 1 and 100, inclusive.
-   All strings in s will have between 1 and 10 characters, inclusive.
-   For each valid i, each character in s[i] will be a lowercase letter ('a'-'z').
 
"""

import collections

class LiveConcert:
    def maxHappiness(self, happiness, idols):
        bestSongs = collections.Counter()
        for i in range(len(happiness)):
            bestSongs[idols[i]] = max(bestSongs[idols[i]], happiness[i])
        return sum(bestSongs.itervalues())


solution = LiveConcert()
cases = [ 
    [[10,5,6,7,1,2], ["ciel","bessie","john","bessie","bessie","john"], 23],
    [[3,3,4,3,3], ["a","a","a","a","a"], 4],
    [[1,2,3,4,5,6,7,8,9,10,100], ["a","b","c","d","e","e","d","c","b","a","abcde"], 140],
    [[100], ["oyusop"], 100],
    [[100,100,100,100,100,100,100,100,100,100,100,100,100], ["haruka","chihaya","yayoi","iori","yukiho","makoto","ami","mami","azusa","miki","hibiki","takane","ritsuko"], 1300]
]

for inp1, inp2, expectedOutput in cases:
    result = solution.maxHappiness(inp1, inp2)
    if result != expectedOutput:
        print "test failed", inp1, inp2, expectedOutput, result
        assert False
