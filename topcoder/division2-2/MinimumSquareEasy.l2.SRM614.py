"""
# [MinimumSquareEasy](http://community.topcoder.com/tc?module=ProblemDetail&rd=15847&pm=12982)
*Single Round Match 614 Round 1 - Division II, Level Two*

## Statement
There are N points in the plane. You are given their description as two int[]s, *x* and *y*, with N elements each. The N points have coordinates (*x*[0],*y*[0]), (*x*[1],*y*[1]), ..., (*x*[N-1],*y*[N-1]).

You want to draw a single square onto the plane. The vertices of the square must have integer coordinates, and the sides of the square must be parallel to the coordinate axes. Additionally, at least N-2 of the N given points must lie strictly inside the square (i.e., not on its boundary).

Return the smallest possible area of a square that satisfies these constraints.

## Definitions
- *Class*: `MinimumSquareEasy`
- *Method*: `minArea`
- *Parameters*: `int[], int[]`
- *Returns*: `long`
- *Method signature*: `long minArea(int[] x, int[] y)`

## Constraints
- *x* will contain between 3 and 50 elements, inclusive.
- *y* will contain the same number of elements as *x*.
- All points will be pairwise distinct.
- Each element of *x* will be between -1,000,000,000 and 1,000,000,000, inclusive.
- Each element of *y* will be between -1,000,000,000 and 1,000,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>[0, 1, 2],<br />[0, 1, 5]</c>
#### Output
<c>4</c>
#### Reason
The square must contain at least one of the three given points. One of the optimal solutions is the square with opposite corners at (-1,-1) and (1,1).

### Example 2
#### Input
<c>[-1, -1, 0, 2, 0],<br />[-2, -1, 0, -1, -2]</c>
#### Output
<c>9</c>
#### Reason
This time the square must contain at least three of the five given points. The optimal solution is the square with opposite corners at (-2,-3) and (1,0).

### Example 3
#### Input
<c>[1000000000, -1000000000, 1000000000, -1000000000],<br />[1000000000, 1000000000, -1000000000, -1000000000]</c>
#### Output
<c>4000000008000000004</c>
#### Reason
In this case one of the optimal solutions is a square that contains all four points.

### Example 4
#### Input
<c>[93, 34, 12, -11, -7, -21, 51, -22, 59, 74, -19, 29, -56, -95, -96, 9, 44, -37, -54, -21],<br />[64, 12, -43, 20, 55, 74, -20, -54, 24, 20, -18, 77, 86, 22, 47, -24, -33, -57, 5, 7]</c>
#### Output
<c>22801</c>


"""

import itertools

def minArea(x, y):
    n = len( x )
    best = float( "inf" )
    for selection in itertools.combinations( zip(x, y), n-2 ):
        minx = min( selection, key = lambda x: x[0] )[0]
        maxx = max( selection, key = lambda x: x[0] )[0]
        miny = min( selection, key = lambda x: x[1] )[1]
        maxy = max( selection, key = lambda x: x[1] )[1]
        cost = max( ( maxx - minx + 2 ), ( maxy - miny + 2 ) )**2
        best = min( best, cost )
    return best
