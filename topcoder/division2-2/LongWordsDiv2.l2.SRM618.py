"""

# [LongWordsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15851&pm=13147)
*Single Round Match 618 Round 1 - Division II, Level Two*

## Statement
Fox Ciel likes all the words that have the following properties:
Each letter of the word is an uppercase English letter.
Equal letters are never consecutive.
There is no subsequence of the form xyxy, where x and y are (not necessarily distinct) letters. Note that a subsequence doesn't have to be contiguous.
Examples:
Ciel does not like "ABBA" because there are two consecutive 'B's.
Ciel does not like "THETOPCODER" because it contains the subsequence "TETE".
Ciel does not like "ABACADA" because it contains the subsequence "AAAA". (Note that here x=y='A'.)
Ciel likes "A", "ABA", and also "ABCBA".
Given a String *word*, return "Likes" (quotes for clarity) if Ciel likes *word* and "Dislikes" if she does not.

## Definitions
- *Class*: `LongWordsDiv2`
- *Method*: `find`
- *Parameters*: `String`
- *Returns*: `String`
- *Method signature*: `String find(String word)`

## Constraints
- *word* will contain between 1 and 100 characters, inclusive.
- Each character of *word* will be an uppercase English letter ('A'-'Z').

## Examples
### Example 1
#### Input
<c>"AAA"</c>
#### Output
<c>"Dislikes"</c>
### Example 2
#### Input
<c>"ABCBA"</c>
#### Output
<c>"Likes"</c>
### Example 3
#### Input
<c>"ABCBAC"</c>
#### Output
<c>"Dislikes"</c>
### Example 4
#### Input
<c>"TOPCODER"</c>
#### Output
<c>"Likes"</c>
### Example 5
#### Input
<c>"VAMOSGIMNASIA"</c>
#### Output
<c>"Dislikes"</c>
### Example 6
#### Input
<c>"SINGLEROUNDMATCH"</c>
#### Output
<c>"Likes"</c>
### Example 7
#### Input
<c>"DALELOBO"</c>
#### Output
<c>"Likes"</c>
"""

def find1(word):
    import itertools
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            return "Dislikes"
    for a,b,c,d in itertools.combinations(word, 4):
        if a == c and b == d:
            return "Dislikes"
    return "Likes"

def isSubSeq( lst, word ):
    index1 = 0
    index2 = 0
    while index2 < len(word) and index1 < len(lst):
        if lst[index1] == word[index2]:
            index1 += 1
        index2 += 1
    return index1 == len(lst)

def find2(word):
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            return "Dislikes"
    import itertools
    import string
    for x, y in itertools.combinations_with_replacement( string.ascii_uppercase, 2 ):
        if isSubSeq( [x, y, x, y], word) or isSubSeq( [y,x,y,x], word):
            return "Dislikes"
    return "Likes"

def find3(word):
    # authors' solution
    import string
    def isSubsequence(a, b):
        i = 0
        j = 0
        while i < len(b) and j < len(a):
            if a[j] == b[i]:
                j += 1
            i += 1
        return j == len(a) 
      
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return "Dislikes"
             
    for X in string.uppercase:
        for Y in string.uppercase:
            if isSubsequence(X+Y+X+Y, word):
                return "Dislikes"
    return "Likes"

def find(word):
    return find1(word)

## try on longer words
#import random, string, itertools
#INPSIZE = 1000000
#NUMCASES = 10
#inp = [ "".join( [x[0] for x in itertools.groupby( [ random.choice(string.ascii_uppercase) for _ in range(INPSIZE) ] ) ] ) for case in range(NUMCASES) ]
#
#import time
#tottime = 0
#for case in inp:
#    before = time.time()
#    res = find(case)
#    tottime += ( time.time() - before )
#
#print tottime
