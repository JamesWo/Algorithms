"""
# [PackingBallsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15842&pm=12995)
*Single Round Match 609 Round 1 - Division II, Level Two*

## Statement
We have *R* red, *G* green, and *B* blue balls.
We want to divide them into as few packages as possible.
Each package must contain 1, 2, or 3 balls.
Additionally, each package must be either a "normal set" (all balls in the package have the same color), or a "variety set" (no two balls have the same color).
Compute and return the smallest possible number of packages.

## Definitions
- *Class*: `PackingBallsDiv2`
- *Method*: `minPacks`
- *Parameters*: `int, int, int`
- *Returns*: `int`
- *Method signature*: `int minPacks(int R, int G, int B)`

## Constraints
- *R*, *G*, and *B* will each be between 1 and 100, inclusive.

## Examples
### Example 1
#### Input
<c>4,<br />2,<br />4</c>
#### Output
<c>4</c>
#### Reason
We have 4 red, 2 green, and 4 blue balls.
Clearly, we need at least four packages to store 10 balls.
One possibility of using exactly four packages looks as follows: RGB, RG, RR, BBB.
(I.e., the first package has 1 ball of each color, the second package has a red and a green ball, and so on.)

### Example 2
#### Input
<c>1,<br />7,<br />1</c>
#### Output
<c>3</c>
#### Reason
Here the only possible solution is to have one package with RGB and two packages with GGG each.

### Example 3
#### Input
<c>2,<br />3,<br />5</c>
#### Output
<c>4</c>
### Example 4
#### Input
<c>78,<br />53,<br />64</c>
#### Output
<c>66</c>
### Example 5
#### Input
<c>100,<br />100,<br />100</c>
#### Output
<c>100</c>

"""

def minPacks(R, G, B):
    total = 0
    minColor = min( R, G, B )
    total += minColor
    rest = []
    rest.append( R - minColor )
    rest.append( G - minColor )
    rest.append( B - minColor )
    rest = filter( lambda x: x != 0, rest )
    if len(rest) == 0:
        return total
    if len(rest) == 1:
        total += (rest[0]+2)/3
    else:
        assert len(rest) == 2
        while rest[0] >= 3 and rest[1] >= 3:
            total += 2
            rest[0] -= 3
            rest[1] -= 3
        minColor, maxColor = min( rest[0], rest[1] ), max( rest[0], rest[1] )
        if minColor == 1:
            total += 1
            maxColor -= 1
        else:
            total += ( 1 if minColor else 0 )
        total += ( ( maxColor + 2 ) / 3 )
    return total
