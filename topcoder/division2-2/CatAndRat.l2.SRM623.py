"""
# [CatAndRat](http://community.topcoder.com/tc?module=ProblemDetail&rd=15856&pm=12932)
*Single Round Match 623 Round 1 - Division II, Level Two*

## Statement
We have a circular tube.
At one point the tube has an entrance.

At time 0, a rat enters the tube via the entrance.
The rat can move inside the tube in both directions (clockwise and counterclockwise).
The rat can change direction in an instant.
Its maximum speed is *Vrat*.

At time *T*, the cat will enter the tube via the same entrance.
The cat can also move in both directions and change its direction instantly.
Its maximum speed is *Vcat*.

For the purpose of this problem, you should imagine the tube as a circle with radius *R*, and the rat and the cat as points on said circle.

The cat is trying to catch the rat as quickly as possible.
The rat is trying not to be caught, and if that is impossible, to be caught as late as possible.
At any time (starting at time 0) the cat and the rat know each other's position.
Already at time 0 the rat knows the time *T*.
Assume that both the cat and the rat behave optimally.

You are given the ints *R*, *T*, *Vrat*, and *Vcat*.
If the cat will catch the rat successfully, return how much time it'll take the cat to catch the rat.
Otherwise, return -1.0.

## Definitions
- *Class*: `CatAndRat`
- *Method*: `getTime`
- *Parameters*: `int, int, int, int`
- *Returns*: `double`
- *Method signature*: `double getTime(int R, int T, int Vrat, int Vcat)`

## Notes
- The cat and rat cannot leave the tube.
- Your return value must have a relative or absolute error less than 1e-9.

## Constraints
- *R*, *T*, *Vrat*, and *Vcat* will each be between 1 and 1000, inclusive.

## Examples
### Example 1
#### Input
<c>10,<br />1,<br />1,<br />1</c>
#### Output
<c>-1.0</c>
#### Reason
The rat can survive. During the first unit of time it has to run away from the entrance. Then, once the cat enters the tube, the rat can always run in the same direction and with the same speed as the cat.

### Example 2
#### Input
<c>10,<br />1,<br />1,<br />2</c>
#### Output
<c>1.0</c>
#### Reason
The cat is now faster than the rat.
The best strategy for the rat is to enter the tube and to start running in either direction at its maximum speed.
The cat will then enter the tube, run in the same direction as the rat, and catch it in exactly 1 unit of time.

### Example 3
#### Input
<c>10,<br />1,<br />2,<br />1</c>
#### Output
<c>-1.0</c>
#### Reason
The rat is now faster than the cat. It can survive, for example by using the strategy described in Example 0.

### Example 4
#### Input
<c>1000,<br />1000,<br />1,<br />1000</c>
#### Output
<c>1.001001001001001</c>
### Example 5
#### Input
<c>1,<br />1000,<br />1,<br />2</c>
#### Output
<c>3.141592653589793</c>


"""
import math

def getTime(R, T, Vrat, Vcat):
    if Vrat >= Vcat:
        return -1
    return min( float(math.pi*R), float(Vrat*T) ) / ( Vcat - Vrat )
