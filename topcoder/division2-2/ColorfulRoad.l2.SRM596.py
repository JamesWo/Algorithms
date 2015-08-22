"""
# [ColorfulRoad](http://community.topcoder.com/tc?module=ProblemDetail&rd=15708&pm=12837)
*Single Round Match 596 Round 1 - Division II, Level Two*

## Statement
There is a one-dimensional road.
The road is separated into N consecutive parts.
The parts are numbered 0 through N-1, in order.
Ciel is going to walk from part 0 to part N-1.

Ciel also noticed that each part of the road has a color: either red, green, or blue.
Part 0 is red.

Ciel is going to perform a sequence of steps.
Each step must lead in the positive direction.
That is, if her current part is i, the next step will take her to one of the parts i+1 through N-1, inclusive.
Her steps can be arbitrarily long.
However, longer steps are harder: a step of length j costs j*j energy.

Additionally, Ciel wants to step on colors in a specific order: red, green, blue, red, green, blue, ...
That is, she starts on the red part 0, makes a step to a green part, from there to a blue part, and so on, always repeating red, green, and blue in a cycle.
Note that the final part N-1 also has some color and thus Ciel must reach it in a corresponding step.

You are given a String *road* containing N elements.
For each i, element i of *road* is the color of part i: 'R' represents red, 'G' green, and 'B' blue.
If Ciel can reach part N-1 in the way described above, return the smallest possible total cost of doing so.
Otherwise, return -1.

## Definitions
- *Class*: `ColorfulRoad`
- *Method*: `getMin`
- *Parameters*: `String`
- *Returns*: `int`
- *Method signature*: `int getMin(String road)`

## Constraints
- *road* will contain between 2 and 15 characters, inclusive.
- Each character of *road* will be either 'R' or 'G' or 'B'.
- The first character of *road* will be 'R'.

## Examples
### Example 1
#### Input
<c>"RGGGB"</c>
#### Output
<c>8</c>
#### Reason
The optimum solution is to step part 0 -> part 2 -> part 4.
The total cost is 2*2 + 2*2 = 8.

### Example 2
#### Input
<c>"RGBRGBRGB"</c>
#### Output
<c>8</c>
#### Reason
The optimum solution is to make steps of length 1.
It costs 1*1 = 1 per each step, so the total cost is 8.

### Example 3
#### Input
<c>"RBBGGGRR"</c>
#### Output
<c>-1</c>
#### Reason
It is impossible to reach the destination.

### Example 4
#### Input
<c>"RBRRBGGGBBBBR"</c>
#### Output
<c>50</c>
### Example 5
#### Input
<c>"RG"</c>
#### Output
<c>1</c>
### Example 6
#### Input
<c>"RBRGBGBGGBGRGGG"</c>
#### Output
<c>52</c>

"""
prevColor = { "R" : "B",
              "G" : "R",
              "B" : "G"
              }

def getMin(road):
    costs = [ 0 for i in range(len(road)) ]
    for i in range(1,len(road)):
        best = float( "inf" )
        for j in range(i):
            if road[j] == prevColor[road[i]]:
                best = min(best, costs[j]+(i-j)*(i-j))
        costs[i] = best
    if costs[-1] != float("inf"):
        return costs[-1]
    else:
        return -1

