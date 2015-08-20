"""
# [MysticAndCandiesEasy](http://community.topcoder.com/tc?module=ProblemDetail&rd=15841&pm=12998)
*Single Round Match 608 Round 1 - Division II, Level Two*

## Statement
TopCoder admin mystic_tc is sitting in front of a table. He found N sealed boxes of candies on the table.

He is not sure how many candies each box contains. However, he knows the following information:
The total number of candies in the boxes is *C*.
For each i, box i (0-based index) contains between 0 and *high*[i] candies, inclusive.

You know that mystic_tc eats candies as follows: first he chooses a subset of the boxes, then he opens them and eats all the candies he found inside.
He wants to eat at least *X* candies.
And as he is smart, he will always choose a subset of boxes for which he is sure that they must contain at least *X* candies.

You are given the ints *C* and *X*, and the int[] *high*.
Return the smallest number of boxes mystic_tc may choose.

## Definitions
- *Class*: `MysticAndCandiesEasy`
- *Method*: `minBoxes`
- *Parameters*: `int, int, int[]`
- *Returns*: `int`
- *Method signature*: `int minBoxes(int C, int X, int[] high)`

## Constraints
- *high* will contain between 1 and 50 elements, inclusive.
- Each element of *high* will be between 1 and 50, inclusive.
- *C* will be between 1 and the sum of all elements of *high*, inclusive.
- *X* will be between 1 and *C*, inclusive.

## Examples
### Example 1
#### Input
<c>10,<br />10,<br />[20]</c>
#### Output
<c>1</c>
#### Reason
There is only one box. It contains all 10 candies. In order to eat 10 candies mystic_tc must open it.

### Example 2
#### Input
<c>10,<br />7,<br />[3, 3, 3, 3, 3]</c>
#### Output
<c>4</c>
#### Reason
Now there are many possibilities for the contents of boxes.
For example, there could be three boxes with 3 candies each, one box with 1 candy, and one empty box.
Another possibility is that there could be five boxes with 2 candies each.
Note that in this case mystic_tc could open three boxes and still get only 6 candies, so he needs to open at least four boxes to be sure he gets at least 7 candies.
And it can be proved that if mystic_tc opens any four of these boxes, they will always contain at least 7 candies in total.

### Example 3
#### Input
<c>100,<br />63,<br />[12, 34, 23, 45, 34]</c>
#### Output
<c>3</c>
#### Reason
Open boxes 1, 3, 4 (0-based). It can be proved that these boxes contain at least 65 candies in total.

### Example 4
#### Input
<c>19,<br />12,<br />[12, 9, 15, 1, 6, 4, 9, 10, 10, 10, 14, 14, 1, 1, 12, 10, 9, 2, 3, 6, 1, 7, 3, 4, 10, 3, 14]</c>
#### Output
<c>22</c>
### Example 5
#### Input
<c>326,<br />109,<br />[9, 13, 6, 6, 6, 16, 16, 16, 10, 16, 4, 3, 10, 8, 11, 17, 12, 5, 7, 8, 7, 4, 15, 7, 14, 2, 2, 1, 17, 1, 7, 7, 12, 17, 2, 9, 7, 1, 8, 16, 7, 4, 16, 2, 13, 3, 13, 1, 17, 6]</c>
#### Output
<c>15</c>

"""

def minBoxes(C, X, high):
    high = sorted( high )
    for i in range( len(high)-1, -1, -1):
        subsum = sum( high[ :i ] )
        diff = C - subsum
        if diff >= X:
            return len(high) - i
    assert False


