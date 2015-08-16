"""
# [PilingRectsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15820&pm=12928)
*Single Round Match 602 Round 1 - Division II, Level Two*

## Statement
Snake Snuke has N rectangles cut out of paper.
The rectangles are labeled 0 through N-1.
You are given int[]s *X* and *Y* with N elements each.
For each i, the sides of rectangle i have lengths *X*[i] and *Y*[i].

Snake Snuke will choose some of his rectangles and place them onto a table, one rectangle at a time, in any order he likes.
Each rectangle (except for the first one) must overlap the immediately previous one, so at the end Snuke will have a pile of rectangles.
Snuke may rotate the rectangles, but once placed, the sides of each rectangle must be parallel to the sides of the table.
(I.e., he may only swap the width and height of some rectangles he places.)
After placing all the rectangles, Snuke computes the area that is covered by all *N* rectangles.
(Formally, the area of their intersection.)

You are also given an int *limit*.
The area computed by Snuke must be greater than or equal to *limit*.

Return the largest positive R such that Snuke can select some R of his rectangles and place them in such a way that the area of their intersection is at least *limit*. If there is no such R, return -1 instead.

## Definitions
- *Class*: `PilingRectsDiv2`
- *Method*: `getmax`
- *Parameters*: `int[], int[], int`
- *Returns*: `int`
- *Method signature*: `int getmax(int[] X, int[] Y, int limit)`

## Constraints
- *X* and *Y* will contain between 1 and 50 elements, inclusive.
- *X* and *Y* will contain the same number of elements.
- Each element of *X* and *Y* will be between 1 and 200, inclusive.
- *limit* will be between 1 and 40000, inclusive.

## Examples
### Example 1
#### Input
<c>[1,2,3,1],<br />[3,2,4,4],<br />3</c>
#### Output
<c>3</c>
#### Reason
He can choose rectangles 0, 2, and 3. These three rectangles can then be placed in such a way that both rectangle 2 and rectangle 3 cover rectangle 0 completely. For this placement, the area of their intersection will be exactly 3.

### Example 2
#### Input
<c>[4,7],<br />[7,4],<br />25</c>
#### Output
<c>2</c>
#### Reason
Note that he can rotate rectangles.

### Example 3
#### Input
<c>[10],<br />[10],<br />9999</c>
#### Output
<c>-1</c>
#### Reason
There is no possible choice.

### Example 4
#### Input
<c>[10],<br />[3],<br />30</c>
#### Output
<c>1</c>
### Example 5
#### Input
<c>[3,6,5,8,2,9,14],<br />[14,6,13,8,15,6,3],<br />27</c>
#### Output
<c>4</c>
### Example 6
#### Input
<c>[121,168,86,106,36,10,125,97,53,26,148,129,41,18,173,55,13,73,91,174,177,190,28,164,122,92,5,26,58,188,14,67,48,196,41,94,24,89,54,117,12,6,155,103,200,128,184,29,92,149],<br />[199,182,43,191,2,145,15,53,38,37,61,45,157,129,119,123,177,178,183,188,132,108,112,137,92,59,75,196,102,152,114,121,181,93,32,3,24,116,4,163,96,159,196,43,59,150,79,113,20,146],<br />5345</c>
#### Output
<c>24</c>

"""
def getmax(X, Y, limit):
    points = []
    best = 0
    for i in range(len(X)):
        points.append( (min(X[i], Y[i]), max(X[i], Y[i]) ) )
    for height in map( lambda x: x[1], points ):
        ans = len( filter(
            lambda x: x[0] >= limit / float(height) and \
                    x[1] >= height, points ) )
        best = max( best, ans )
    return best if best else -1

