"""
# [NextOrPrev](http://community.topcoder.com/tc?module=ProblemDetail&rd=15492&pm=12454)
*Single Round Match 572 Round 1 - Division II, Level Two*

## Statement
Consider a string consisting of lowercase characters and following two operations that can change it: 
Next: Choose a lowercase character other than 'z' and replace its every occurrence with the next character 
	('a' -> 'b', 'b' -> 'c', ..., 'x' -> 'y', 'y' -> 'z').
	Prev: Choose a lowercase character other than 'a' and replace its every occurrence with the previous character 
	('b' -> 'a', 'c' -> 'b', ..., 'y' -> 'x', 'z' -> 'y').
You can use each operation as many times as you want, and in any order you like. 
You are given ints *nextCost* and *prevCost*. 
These represent the cost of using each Next and Prev operation, respectively. 
You are also given two Strings *start* and *goal*. 
These strings are special: no two characters in *start* are the same, and no two characters in *goal* are the same. 
Return the minimum cost required in order to transform *start* into *goal* using the above operations. 
If transforming *start* into *goal* is impossible, return -1 instead.

## Definitions
- *Class*: `NextOrPrev`
- *Method*: `getMinimum`
- *Parameters*: `int, int, String, String`
- *Returns*: `int`
- *Method signature*: `int getMinimum(int nextCost, int prevCost, String start, String goal)`

## Constraints
- *nextCost* and *prevCost* will each be between 1 and 1000, inclusive.
- *start* and *goal* will each contain between 1 and 26 characters, inclusive.
- *start* and *goal* will contain the same number of characters.
- Each character in *start* and *goal* will be a lowercase character.
- The characters in *start* will be distinct.
- The characters in *goal* will be distinct.

## Examples
### Example 1
#### Input
<c>5,<br />8,<br />"ae",<br />"bc"</c>
#### Output
<c>21</c>
#### Reason
There are several optimal sequences of operations. 
Here is one of them: "ae" -(Next)-> "be" -(Prev)-> "bd" -(Prev)-> "bc". The total cost is 5 + 8 + 8 = 21.

### Example 2
#### Input
<c>5,<br />8,<br />"ae",<br />"cb"</c>
#### Output
<c>-1</c>
#### Reason
It is impossible to transform "ae" into "cb".

### Example 3
#### Input
<c>1,<br />1,<br />"srm",<br />"srm"</c>
#### Output
<c>0</c>
#### Reason
*start* and *goal* may be the same. 
The cost of an empty sequence of operations is 0.

### Example 4
#### Input
<c>10,<br />1,<br />"acb",<br />"bdc"</c>
#### Output
<c>30</c>
### Example 5
#### Input
<c>10,<br />1,<br />"zyxw",<br />"vuts"</c>
#### Output
<c>16</c>
### Example 6
#### Input
<c>563,<br />440,<br />"ptrbgcnlaizo",<br />"rtscedkiahul"</c>
#### Output
<c>10295</c>
### Example 7
#### Input
<c>126,<br />311,<br />"yovlkwpjgsna",<br />"zpwnkytjisob"</c>
#### Output
<c>-1</c>

"""
def getMinimum(nextCost, prevCost, start, goal):
    for i in range(len(start)):
        for j in range(len(start)):
            if i == j:
                continue
            if start[i]<start[j] and goal[i]>goal[j]:
                return -1
            if start[i]>start[j] and goal[i]<goal[j]:
                return -1
            if start[i] < goal[j] < goal[i] < start[j]:
                return -1

    totCost = 0
    for i in range(len(start)):
        char1 = start[i]
        char2 = goal[i]
        if char1 < char2:
            totCost += (ord(char2)-ord(char1))*nextCost
        elif char1 >= char2:
            totCost += (ord(char1)-ord(char2))*prevCost
    return totCost


