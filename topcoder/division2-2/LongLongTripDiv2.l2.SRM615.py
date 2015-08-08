"""
# [LongLongTripDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15848&pm=13091)
*Single Round Match 615 Round 1 - Division II, Level Two*

## Statement
Limit is a flea. He can do two types of jumps: small jumps that have length 1 millimeter, and big jumps that have length *B* millimeters.

Limit is going to make exactly *T* jumps, all of them in the same direction. He would like to travel exactly *D* millimeters in those jumps. Is this possible?

You are given a long *D*, and ints *T* and *B*. Return "Possible" (quotes for clarity) if there is a combination of *T* jumps forward that has a total length of exactly *D* millimeters. Otherwise, return "Impossible".

## Definitions
- *Class*: `LongLongTripDiv2`
- *Method*: `isAble`
- *Parameters*: `long, int, int`
- *Returns*: `String`
- *Method signature*: `String isAble(long D, int T, int B)`

## Constraints
- *D* will be between 1 and 10^18, inclusive.
- *T* will be between 1 and 1,000,000,000, inclusive.
- *B* will be between 2 and 1,000,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>10,<br />6,<br />3</c>
#### Output
<c>"Possible"</c>
#### Reason
Limit must make 6 jumps that have a total length of 10 millimeters. This is possible: two of the jumps must be long and the other four must be short.

### Example 2
#### Input
<c>10,<br />5,<br />3</c>
#### Output
<c>"Impossible"</c>
### Example 3
#### Input
<c>50,<br />100,<br />2</c>
#### Output
<c>"Impossible"</c>
### Example 4
#### Input
<c>120,<br />10,<br />11</c>
#### Output
<c>"Impossible"</c>
### Example 5
#### Input
<c>10,<br />10,<br />9999</c>
#### Output
<c>"Possible"</c>
### Example 6
#### Input
<c>1000,<br />100,<br />10</c>
#### Output
<c>"Possible"</c>
### Example 7
#### Input
<c>1000010000100001,<br />1100011,<br />1000000000</c>
#### Output
<c>"Possible"</c>
"""


def isAble(D, T, B):
    # binary search for the number of large jumps required
    lo = 0 # all small jumps
    hi = T # all large jumps
    while lo < hi:
        mid = ( lo + hi ) / 2
        dist = ( mid * B ) + ( T - mid )
        if dist < D:
            lo = mid + 1
        else:
            hi = mid
    assert lo == hi
    return "Possible" if ( ( lo * B ) + ( T - lo ) == D ) else "Impossible"


