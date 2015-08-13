"""
# [PowerOfThreeEasy](http://community.topcoder.com/tc?module=ProblemDetail&rd=15837&pm=12952)
*Single Round Match 604 Round 1 - Division II, Level Two*

## Statement
Fox Ciel has a robot.
The robot is located on an infinite plane.
At the beginning, the robot starts at the coordinates (0, 0).
The robot can then make several steps.
The steps are numbered starting from 0.

In each step, Ciel must choose one of two directions for the robot: right (x coordinate increases) or up (y coordinate increases).
In step k, the robot will move 3^k units in the chosen direction.
It is not allowed to skip a step.

You are given ints *x* and *y*.
Return "Possible" (quotes for clarity) if it is possible that the robot reaches the point (*x*,*y*) after some (possibly zero) steps.
Otherwise, return "Impossible".

## Definitions
- *Class*: `PowerOfThreeEasy`
- *Method*: `ableToGet`
- *Parameters*: `int, int`
- *Returns*: `String`
- *Method signature*: `String ableToGet(int x, int y)`

## Constraints
- *x* will be between 0 and 1,000,000,000, inclusive.
- *y* will be between 0 and 1,000,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>1,<br />3</c>
#### Output
<c>"Possible"</c>
#### Reason
In step 0 Ciel will send the robot right to (1,0). In step 1 she will send it up to (1,3).

### Example 2
#### Input
<c>1,<br />1</c>
#### Output
<c>"Impossible"</c>
### Example 3
#### Input
<c>3,<br />0</c>
#### Output
<c>"Impossible"</c>
### Example 4
#### Input
<c>1,<br />9</c>
#### Output
<c>"Impossible"</c>
#### Reason
Note that it is not allowed to move the robot right in step 0, skip step 1, and then move the robot up in step 2.

### Example 5
#### Input
<c>3,<br />10</c>
#### Output
<c>"Possible"</c>
### Example 6
#### Input
<c>1093,<br />2187</c>
#### Output
<c>"Possible"</c>
### Example 7
#### Input
<c>0,<br />0</c>
#### Output
<c>"Possible"</c>
"""

def able(x, y, startx, starty, time):
    if startx == x and starty == y:
        return True
    if startx > x or starty > y:
        return False
    return ( able(x, y, startx + time, starty, time*3 ) or \
             able(x, y, startx, starty + time, time*3 ) )


def ableToGet(x, y):
    if able(x, y, 0, 0, 1):
        return "Possible"
    return "Impossible"
