"""
# [TheNumberGameDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15494&pm=12485)
*Single Round Match 574 Round 1 - Division II, Level Two*

## Statement
Manao has recently invented a brand new single-player game called The Number Game.

The player starts with a number *A*. Also, another number *B* is chosen. Note that neither *A* nor *B* contain a zero digit in their base 10 representation.

The player's goal is to obtain *B* from *A*. In each move, the player can either reverse his current number, or he can divide it by 10 (using integer division).
For example, if the current number is 12849, the player can either reverse it to obtain 94821, or he can divide it by 10 to obtain 1284. (Note that we always round down when using integer division.)

You are given two ints *A* and *B*. If it is possible to obtain *B* from *A*, return the minimum number of moves necessary to reach this goal. Otherwise, return -1.

## Definitions
- *Class*: `TheNumberGameDiv2`
- *Method*: `minimumMoves`
- *Parameters*: `int, int`
- *Returns*: `int`
- *Method signature*: `int minimumMoves(int A, int B)`

## Constraints
- *A* will be between 1 and 999,999,999, inclusive.
- *B* will be between 1 and 999,999,999, inclusive.
- *A* and *B* will not contain a zero digit in base 10 representation.
- *A* and *B* will be distinct.

## Examples
### Example 1
#### Input
<c>25,<br />5</c>
#### Output
<c>2</c>
#### Reason
Initially, the player has number 25 and needs to obtain 5. He can reverse the number and obtain 52, then divide it by 10 and obtain 5.

### Example 2
#### Input
<c>5162,<br />16</c>
#### Output
<c>4</c>
#### Reason
To obtain 16 from 5162 in four moves, the player can perform the following sequence of moves:

Reverse the number and obtain 2615.
Divide 2615 by 10 and obtain 261.
Reverse 261 and obtain 162.
Divide 162 by 10 and obtain 16.
Note that this is not the only possible sequence of four moves which leads to the goal.

### Example 3
#### Input
<c>334,<br />12</c>
#### Output
<c>-1</c>
#### Reason
There is no way to obtain 12 from 334.

### Example 4
#### Input
<c>218181918,<br />9181</c>
#### Output
<c>6</c>
### Example 5
#### Input
<c>9798147,<br />79817</c>
#### Output
<c>-1</c>

"""
def rev(x):
    return int(str(x)[::-1])

def minimumMovesHelper(A, B):
    if A == 0:
        return float("inf")
    if A == B:
        return 0
    if rev(A) == B:
        return 1
    a1 = minimumMovesHelper(A/10, B) + 1
    a2 = minimumMovesHelper(rev(A)/10, B) + 2
    return min(a1, a2)

def minimumMoves(A, B):
    res = minimumMovesHelper(A, B)
    if res == float("inf"):
        return -1
    return res
