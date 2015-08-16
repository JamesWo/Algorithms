"""
# [PairGameEasy](http://community.topcoder.com/tc?module=ProblemDetail&rd=15853&pm=13161)
*Single Round Match 620 Round 1 - Division II, Level Two*

## Statement
You have an ordered pair of integers.
You can now make zero or more steps.
In each step, you can change your pair into a new pair of integers by adding one of them to the other.
That is, if your current pair is (x, y), then your next pair will be either (x+y, y), or (x, x+y).

For example, you can start with (1, 2), change it to (3, 2), change that to (3, 5), and then change that again to (3, 8).

You are given four ints: *a*, *b*, *c*, and *d*.
Return "Able to generate" (quotes for clarity) if it is possible to start with the pair (*a*, *b*) and end with the pair (*c*, *d*).
Otherwise, return "Not able to generate".

## Definitions
- *Class*: `PairGameEasy`
- *Method*: `able`
- *Parameters*: `int, int, int, int`
- *Returns*: `String`
- *Method signature*: `String able(int a, int b, int c, int d)`

## Constraints
- *a* will be between 1 and 1,000, inclusive.
- *b* will be between 1 and 1,000, inclusive.
- *c* will be between 1 and 1,000, inclusive.
- *d* will be between 1 and 1,000, inclusive.

## Examples
### Example 1
#### Input
<c>1,<br />2,<br />3,<br />5</c>
#### Output
<c>"Able to generate"</c>
#### Reason
(1, 2) -> (3, 2) -> (3, 5).

### Example 2
#### Input
<c>1,<br />2,<br />2,<br />1</c>
#### Output
<c>"Not able to generate"</c>
#### Reason
Note that order matters: (1, 2) and (2, 1) are two different pairs.

### Example 3
#### Input
<c>2,<br />2,<br />2,<br />999</c>
#### Output
<c>"Not able to generate"</c>
### Example 4
#### Input
<c>2,<br />2,<br />2,<br />1000</c>
#### Output
<c>"Able to generate"</c>
### Example 5
#### Input
<c>47,<br />58,<br />384,<br />221</c>
#### Output
<c>"Able to generate"</c>
### Example 6
#### Input
<c>1000,<br />1000,<br />1000,<br />1000</c>
#### Output
<c>"Able to generate"</c>
"""
import sys
sys.setrecursionlimit( 5000 )

def ableHelper(a, b, c, d):
    if (a, b) == (c, d):
        return True
    if (a > c) or (b > d):
        return False
    return ableHelper( a+b, b, c, d ) or ableHelper(a, a+b, c, d)

def able(a, b, c, d):
    if ableHelper(a, b, c, d):
        return "Able to generate"
    else:
        return "Not able to generate"
