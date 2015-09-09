"""
# [AlternateColors](http://community.topcoder.com/tc?module=ProblemDetail&rd=15186&pm=12343)
*Single Round Match 564 Round 1 - Division II, Level Two*

## Statement
Bob is playing with his ball destroyer robot. Initially, Bob has *r* red balls, *g* green balls and *b* blue balls. The robot will repeat the following 3-step program until there are no balls left:

If there is at least one red ball available, destroy one red ball.
If there is at least one green ball available, destroy one green ball.
If there is at least one blue ball available, destroy one blue ball.
You are given the longs *r*, *g* and *b*. You are also given a long *k*. Find the color of the *k*-th ball (1-index based) that will be destroyed.
If the color of the *k*-th ball to be destroyed is red, return "RED" (quotes for clarity, returned values are case-sensitive).
If the color is green, return "GREEN".
If the color is blue, return "BLUE".

## Definitions
- *Class*: `AlternateColors`
- *Method*: `getColor`
- *Parameters*: `long, long, long, long`
- *Returns*: `String`
- *Method signature*: `String getColor(long r, long g, long b, long k)`

## Constraints
- *r*, *g* and *b*  will each be between 1 and 1000000000000 (10^12), inclusive.
- *k* will be between 1 and *r*+*g*+*b*, inclusive.

## Examples
### Example 1
#### Input
<c>1,<br />1,<br />1,<br />3</c>
#### Output
<c>"BLUE"</c>
#### Reason
The order in which the balls are destroyed is: Red, green and blue. The third ball was blue.

### Example 2
#### Input
<c>3,<br />4,<br />5,<br />4</c>
#### Output
<c>"RED"</c>
#### Reason
The order in which the balls are destroyed is:  Red, green, blue, red, green, blue, red, green, blue, green, blue and blue.

### Example 3
#### Input
<c>7,<br />7,<br />1,<br />7</c>
#### Output
<c>"GREEN"</c>
### Example 4
#### Input
<c>1000000000000,<br />1,<br />1,<br />1000000000002</c>
#### Output
<c>"RED"</c>
#### Reason
Once the only green and blue balls are destroyed, all of the remaining balls will be red.

### Example 5
#### Input
<c>653,<br />32,<br />1230,<br />556</c>
#### Output
<c>"BLUE"</c>

"""
def getColorTwo(x, y, k):
    if ( k/2 ) < min(x,y):
        return (k-1)%2
    if x < y:
        return 1
    else:
        return 0

def getColor(r, g, b, k):
    if ( (k-1)/3 ) < min(r,g,b):
        mapping = {0:"RED", 1:"GREEN", 2:"BLUE"}
        return mapping[(k-1)%3]
    m = min(r,g,b)
    if r-m == 0:
        if getColorTwo(g-m, b-m, k-3*m) == 0:
            return "GREEN"
        else:
            return "BLUE"
    if g-m == 0:
        if getColorTwo(r-m, b-m, k-3*m) == 0:
            return "RED"
        else:
            return "BLUE"
    if b-m == 0:
        if getColorTwo(r-m, g-m, k-3*m) == 0:
            return "RED"
        else:
            return "GREEN"
    else:
        assert False
        
