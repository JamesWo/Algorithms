"""
# [LittleElephantAndString](http://community.topcoder.com/tc?module=ProblemDetail&rd=15709&pm=12854)
*Single Round Match 597 Round 1 - Division I, Level One*

## Statement
Little Elephant from the Zoo of Lviv likes strings.

You are given a String *A* and a String *B* of the same length. In one turn Little Elephant can choose any character of *A* and move it to the beginning of the string (i.e., before the first character of *A*). Return the minimal number of turns needed to transform *A* into *B*. If it's impossible, return -1 instead.

## Definitions
- *Class*: `LittleElephantAndString`
- *Method*: `getNumber`
- *Parameters*: `String, String`
- *Returns*: `int`
- *Method signature*: `int getNumber(String A, String B)`

## Constraints
- *A* will contain between 1 and 50 characters, inclusive.
- *B* will contain between 1 and 50 characters, inclusive.
- *A* and *B* will be of the same length.
- *A* and *B* will consist of uppercase letters ('A'-'Z') only.

## Examples
### Example 1
#### Input
<c>"ABC",<br />"CBA"</c>
#### Output
<c>2</c>
#### Reason
The optimal solution is to make two turns. On the first turn, choose character 'B' and obtain string "BAC". On the second turn, choose character 'C' and obtain "CBA".

### Example 2
#### Input
<c>"A",<br />"B"</c>
#### Output
<c>-1</c>
#### Reason
In this case, it's impossible to transform *A* into *B*.

### Example 3
#### Input
<c>"AAABBB",<br />"BBBAAA"</c>
#### Output
<c>3</c>
### Example 4
#### Input
<c>"ABCDEFGHIJKLMNOPQRSTUVWXYZ",<br />"ZYXWVUTSRQPONMLKJIHGFEDCBA"</c>
#### Output
<c>25</c>
### Example 5
#### Input
<c>"A",<br />"A"</c>
#### Output
<c>0</c>
### Example 6
#### Input
<c>"DCABA",<br />"DACBA"</c>
#### Output
<c>2</c>

"""
def getNumber(A, B):
    if sorted(A) != sorted(B):
        return -1
    i = j = len(A)-1
    while i >= 0:
        char = B[j]
        while True:
            if i < 0:
                return j+1
            if A[i] != char:
                i -= 1
            else:
                break
        i -= 1
        j -= 1
    return j + 1
