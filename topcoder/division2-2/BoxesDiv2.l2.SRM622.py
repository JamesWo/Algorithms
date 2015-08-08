"""
# [BoxesDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15855&pm=13192)
*Single Round Match 622 Round 1 - Division II, Level Two*

## Statement
Today is Fox Ciel's birthday.
You want to give her a box of candies as a present.

You have candies of several different types.
You are given a int[] *candyCounts*.
Each element of *candyCounts* is the number of candies of one particular type.

For each non-negative integer i, you have an unlimited supply of boxes with volume 2^i.
That is, you have boxes with volume 1, 2, 4, 8, and so on.

You are going to pack the candies into boxes.
Each type of candies has to be packed into a single box, and you have to use different boxes for different types of candy.
The volume of a box must be greater than or equal to the number of candies it contains.

Once you have each type of candies in a box, you want to pack those boxes into larger boxes, until only one box remains.
You can only pack two boxes at a time.
That is, you can take any two boxes you currently have, get a new box, and put the two old boxes into the new box.
This is possible if and only if the volume of the new box is greater than or equal to the sum of volumes of the two old boxes.
You always get to choose which two boxes you want to pack together, and how large the new box should be.

To summarize:
First, you will pack all the candies into boxes.
Then, you will pack all those boxes into larger boxes, until you are left with a single box that contains everything.

Compute and return the smallest possible volume of the box obtained at the end of packing.

## Definitions
- *Class*: `BoxesDiv2`
- *Method*: `findSize`
- *Parameters*: `int[]`
- *Returns*: `int`
- *Method signature*: `int findSize(int[] candyCounts)`

## Notes
- You may assume that the return value always fits into a signed 32-bit integer variable.

## Constraints
- *candyCounts* will contain between 1 and 100 elements, inclusive.
- Each element of *candyCounts* will be between 1 and 1000, inclusive.

## Examples
### Example 1
#### Input
<c>[8,8]</c>
#### Output
<c>16</c>
#### Reason
First, you pack each type of candies into a box with volume 8. Then, you pack the two boxes into a single box with volume 16.

### Example 2
#### Input
<c>[5,6]</c>
#### Output
<c>16</c>
#### Reason
Even though you have fewer candies than in Example 0, you still have to use boxes with volume 8 (or more) to store them.

### Example 3
#### Input
<c>[1,7]</c>
#### Output
<c>16</c>
#### Reason
Now you could pack the 1 candy into a smaller box, but it will not help: you still have to use a box with volume 16 to store the two boxes with candies.

### Example 4
#### Input
<c>[1,1,13,1,1]</c>
#### Output
<c>32</c>
### Example 5
#### Input
<c>[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]</c>
#### Output
<c>1024</c>
"""
global smallest
smallest = 1

def getSmallest(d):
    global smallest
    if smallest not in d:
        smallest <<= 1
        return getSmallest(d)
    if d[smallest] == 0:
        d.pop(smallest)
        smallest <<= 1
        return getSmallest(d)
    if d[smallest] == 1:
        d.pop(smallest)
    else:
        d[smallest] -= 1
    return smallest

def getNextMultiple(i):
    return 1 << (i-1).bit_length()

def findSize(candyCounts):
    # round each candyCount to the next multiple of 2
    candyCounts = map( getNextMultiple, candyCounts )
    counts = {}
    for v in candyCounts:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    smallest = 1
    while True:
        # take the two smallest boxes and combine them
        if len(counts) == 1 and counts[ counts.keys()[0] ] == 1:
            return counts.keys()[0]
        getSmallest(counts)
        secondSmallest = getSmallest(counts)
        new = secondSmallest << 1
        if new not in counts:
            counts[new] = 1
        else:
            counts[new] += 1


