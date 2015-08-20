"""
# [GearsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15701&pm=12732)
*Single Round Match 589 Round 1 - Division II, Level Two*

## Statement
Goose Tattarrattat has a machine that contains N gears (cogwheels).
The gears are numbered 0 through N-1.
Currently, the gears are arranged into a cycle: for each i, gear i meshes with gears i-1 and i+1 (counting modulo N).
In particular, gear 0 meshes with gear N-1.

Let X and Y be two meshing gears.
Note that if X is turning, Y must clearly be turning in the opposite direction (clockwise vs. counter-clockwise).

For each of the N gears we have a desired direction of turning.
You are given this information encoded as a String *Directions*.
Character i of *Directions* is 'R' if we want gear i to turn to the right (clockwise), and it is 'L' if we want it to turn to the left.

Of course, it may be impossible to satisfy all the desired directions of turning.
Return the minimal number of gears that have to be removed from the machine so that all remaining gears can turn in the desired directions at the same time.

## Definitions
- *Class*: `GearsDiv2`
- *Method*: `getmin`
- *Parameters*: `String`
- *Returns*: `int`
- *Method signature*: `int getmin(String Directions)`

## Notes
- Removing a gear creates a gap between the other gears. For example, after removing the gear 7, gears 6 and 8 will not mesh.

## Constraints
- *Directions* will contain between 3 and 50 characters, inclusive.
- Each character of *Directions* will be 'R' or 'L'.

## Examples
### Example 1
#### Input
<c>"LRRR"</c>
#### Output
<c>1</c>
#### Reason
Once we remove gear 2, the other three are free to turn in the desired directions.

### Example 2
#### Input
<c>"RRR"</c>
#### Output
<c>2</c>
#### Reason
Gear 0 meshes with gear 2.

### Example 3
#### Input
<c>"LRLR"</c>
#### Output
<c>0</c>
### Example 4
#### Input
<c>"LRLLRRLLLRRRLLLL"</c>
#### Output
<c>6</c>
### Example 5
#### Input
<c>"RRRRRRRLRRRRRRRLRLRLLRLRLRLRRLRLRLLLRLRLLRLLRRLRRR"</c>
#### Output
<c>14</c>

"""
def getmin(Directions):
    d=[]
    n = len(Directions)
    if "L" not in Directions or "R" not in Directions:
        return ( n + 1 ) / 2
    if "LR" in Directions:
        firstL = Directions.index( "LR" )
    else:
        firstL = Directions.index( "RL" )
    for i in range(n):
        d.append( Directions[ ( i + firstL + 1) % n ] )
    for i in range(1, n):
        if d[i] == d[i-1]:
            d[i] = "X"

    return d.count( "X" )

