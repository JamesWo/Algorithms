"""
# [TaroFriends](http://community.topcoder.com/tc?module=ProblemDetail&rd=15846&pm=13005)
*Single Round Match 613 Round 1 - Division I, Level One*

## Statement
Cat Taro likes to play with his cat friends.
Each of his friends currently sits on some coordinate on a straight line that goes from the left to the right.
When Taro gives a signal, each of his friends must move exactly *X* units to the left or to the right.

You are given an int[] *coordinates* and the int *X*.
For each i, the element *coordinates*[i] represents the coordinate of the i-th cat before the movement.
Return the smallest possible difference between the positions of the leftmost cat and the rightmost cat after the movement.

## Definitions
- *Class*: `TaroFriends`
- *Method*: `getNumber`
- *Parameters*: `int[], int`
- *Returns*: `int`
- *Method signature*: `int getNumber(int[] coordinates, int X)`

## Constraints
- *coordinates* will contain between 1 and 50 elements, inclusive.
- Each element of *coordinates* will be between -100,000,000 and 100,000,000, inclusive.
- *X* will be between 0 and 100,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>[-3, 0, 1],<br />3</c>
#### Output
<c>3</c>
#### Reason
The difference 3 is obtained if the cats move from {-3,0,1} to {0,-3,-2}.

![image](images/img01.png)

### Example 2
#### Input
<c>[4, 7, -7],<br />5</c>
#### Output
<c>4</c>
#### Reason
The difference 4 is obtained if the cats move from {4,7,-7} to {-1,2,-2}.

![image](images/img02_new.png)

### Example 3
#### Input
<c>[-100000000, 100000000],<br />100000000</c>
#### Output
<c>0</c>
### Example 4
#### Input
<c>[3, 7, 4, 6, -10, 7, 10, 9, -5],<br />7</c>
#### Output
<c>7</c>
### Example 5
#### Input
<c>[-4, 0, 4, 0],<br />4</c>
#### Output
<c>4</c>
### Example 6
#### Input
<c>[7],<br />0</c>
#### Output
<c>0</c>
"""

def getNumber(coordinates, X):
    # the crucial insight here is that in the optimal solution, 
    # consecutive cats will move in the same direction,
    # except for one pair. 
    coordinates.sort()
    best = 1000000000
    for split in range(len(coordinates)):
        left = coordinates[:split]
        right = coordinates[split:]
        newPos = map(lambda y:y+X, left) + map(lambda y: y-X, right)
        best = min(best, max(newPos)-min(newPos) )
    return best
