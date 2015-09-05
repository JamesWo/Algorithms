"""
# [RobotHerbDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15490&pm=12425)
*Single Round Match 570 Round 1 - Division II, Level Two*

## Statement
Robot Herb is playing on an infinite square grid.
At any moment, Herb stands on one of the squares and he faces one of the four cardinal directions.
In his memory, Herb has a program.
The program is a sequence of commands.
For each i, the i-th of these commands has the following form:

First move forward *a*[i] tiles.
Then turn 90 degrees to the right, *a*[i] times in a row.

Herb has decided to run the program *T* times.
You are given the int *T* and the int[] *a* that describes Herb's program.
Let A be the initial position of Herb and B be his position after the program was executed *T* times. Return the Manhattan distance between tiles A and B.

## Definitions
- *Class*: `RobotHerbDiv2`
- *Method*: `getdist`
- *Parameters*: `int, int[]`
- *Returns*: `int`
- *Method signature*: `int getdist(int T, int[] a)`

## Notes
- Let's introduce a Cartesian coordinate system on the grid so that each cardinal direction is parallel to one of the axes. The Manhattan distance between two tiles with centers at points (x1, y1) and (x2, y2) is defined as |x1-x2| + |y1-y2|.

## Constraints
- *T* will be between 1 and 100, inclusive.
- *a* will contain between 1 and 50 elements, inclusive.
- Each element of *a* will be between 1 and 400,000, inclusive.

## Examples
### Example 1
#### Input
<c>1,<br />[1,2,3]</c>
#### Output
<c>2</c>
#### Reason
Suppose that initially Herb stands on the tile with center at (0, 0) and faces the positive y direction. The program will get executed as follows:
tile         direction
After 1st command:     (0, 1)       positive x
After 2nd command:     (2, 1)       negative x
After 3rd command:     (-1, 1)      negative y
The manhattan distance between the initial and the final positions is |-1| + |1| = 2.

### Example 2
#### Input
<c>100,<br />[1]</c>
#### Output
<c>0</c>
### Example 3
#### Input
<c>5,<br />[1,1,2]</c>
#### Output
<c>10</c>
### Example 4
#### Input
<c>100,<br />[400000]</c>
#### Output
<c>40000000</c>

"""
def getdist(T, a):
    pos = [0,0]
    direction = 0 #north
    for i in range(len(a)):
        if direction == 0:
            pos[1] += a[i]
        elif direction == 1:
            pos[0] += a[i]
        elif direction == 2:
            pos[1] -= a[i]
        elif direction == 3:
            pos[0] -= a[i]
        else:
            assert False
        direction += a[i]
        direction %= 4
    newPos = [0,0]
    newdirection = 0
    for _ in range(T):
        if newdirection == 0:
            newPos[0] += pos[0]
            newPos[1] += pos[1]
        elif newdirection == 1:
            newPos[0] += pos[1]
            newPos[1] -= pos[0]
        elif newdirection == 2:
            newPos[0] -= pos[0]
            newPos[1] -= pos[1]
        elif newdirection == 3:
            newPos[0] -= pos[1]
            newPos[1] += pos[0]
        newdirection += direction
        newdirection %= 4
    return abs(newPos[0]) + abs(newPos[1])

