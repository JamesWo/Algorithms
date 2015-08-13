"""
# [SplitIntoPairs](http://community.topcoder.com/tc?module=ProblemDetail&rd=15836&pm=12939)
*Single Round Match 603 Round 1 - Division II, Level Two*

## Statement
You are given a int[] *A* with N elements, where N is even.
Note that some elements of *A* may be negative.
You are also given a int *X* which is guaranteed to be negative.
You must divide the elements of *A* into N/2 disjoint pairs.
(That is, each element of *A* must be in exactly one of those pairs.)
Your goal is to maximize the number of pairs in which the product of the two elements is greater than or equal to *X*.
Return the largest possible number of such pairs.

## Definitions
- *Class*: `SplitIntoPairs`
- *Method*: `makepairs`
- *Parameters*: `int[], int`
- *Returns*: `int`
- *Method signature*: `int makepairs(int[] A, int X)`

## Constraints
- *A* will contain between 2 and 50 elements, inclusive.
- The number of elements in *A* will be even.
- Each element in *A* will be between -1,000,000,000 and 1,000,000,000, inclusive.
- *X* will be between -1,000,000,000 and -1, inclusive.

## Examples
### Example 1
#### Input
<c>[2,-1],<br />-1</c>
#### Output
<c>0</c>
#### Reason
One possible pair has product -2, which is lower than needed.

### Example 2
#### Input
<c>[1,-1],<br />-1</c>
#### Output
<c>1</c>
#### Reason
Here product is -1, it's enough.

### Example 3
#### Input
<c>[-5,-4,2,3],<br />-1</c>
#### Output
<c>2</c>
#### Reason
If first pair contains numbers -5 and -4, and second contains 2 and 3, both will have positive product.

### Example 4
#### Input
<c>[5,-7,8,-2,-5,3],<br />-7</c>
#### Output
<c>3</c>
#### Reason
Acceptable splitting is {5,8}, {-7,-5} and {-2,3}.

### Example 5
#### Input
<c>[3,4,5,6,6,-6,-4,-10,-1,-9],<br />-2</c>
#### Output
<c>4</c>
### Example 6
#### Input
<c>[1000000,1000000],<br />-5</c>
#### Output
<c>1</c>
#### Reason
Beware overflow.
"""

def makepairs(A, X):
    numPos = len( filter( lambda x: x > 0, A ) )
    numNeg = len( filter( lambda x: x < 0, A ) )
    numZero = A.count( 0 )
    if numPos % 2 == 0 or numNeg % 2 == 0 or numZero == 2:
        return len(A)/2
    minPos = min( filter( lambda x: x > 0, A ) )
    maxNeg = max( filter( lambda x: x < 0, A ) )
    if ( minPos * maxNeg ) >= X:
        return len(A)/2
    else:
        return (len(A)/2)-1
