"""
# [PenguinPals](http://community.topcoder.com/tc?module=ProblemDetail&rd=15486&pm=12355)
*Single Round Match 566 Round 1 - Division II, Level Two*

## Statement
Penguin Pals is a match making service that matches penguins to new friends, using the following procedure:

Each penguin is asked a single question: "Do you prefer the color blue, or the color red?"
All penguins are arranged so that they stand on a circle, equally spaced. 
The organizers draw some straight lines, connecting some pairs of penguins. Each penguin may only be connected to at most one other penguin. Two penguins cannot be connected if they prefer a different color.
Each penguin who is connected to some other penguin follows the line to find their match.

The only problem with the above system was that it allowed penguins to collide if two lines crossed each other.
Therefore, a new additional rule was adopted: no two lines may cross.
Penguin Pals now has some penguins arranged on a circle (after step 2 of the above procedure).
They need to know the maximum number of pairs of penguins they can create.

You are given a String *colors* whose i-th character represents the prefered color of the i-th penguin (0-based index) in the circular arrangement. The i-th character is 'R' if the i-th penguin prefers red and 'B' if the i-th penguin prefers blue. Return the maximum number of matched pairs that can be formed.

## Definitions
- *Class*: `PenguinPals`
- *Method*: `findMaximumMatching`
- *Parameters*: `String`
- *Returns*: `int`
- *Method signature*: `int findMaximumMatching(String colors)`

## Constraints
- *colors* will contain between 1 and 50 characters, inclusive.
- Each character of *colors* will be either 'R' or 'B'.

## Examples
### Example 1
#### Input
<c>"RRBRBRBB"</c>
#### Output
<c>3</c>
#### Reason
In this picture the penguins have been colored in their preferred color. 

![image](images/ex0.png)

### Example 2
#### Input
<c>"RRRR"</c>
#### Output
<c>2</c>
### Example 3
#### Input
<c>"BBBBB"</c>
#### Output
<c>2</c>
### Example 4
#### Input
<c>"RBRBRBRBR"</c>
#### Output
<c>4</c>
### Example 5
#### Input
<c>"RRRBRBRBRBRB"</c>
#### Output
<c>5</c>
### Example 6
#### Input
<c>"R"</c>
#### Output
<c>0</c>
### Example 7
#### Input
<c>"RBRRBBRB"</c>
#### Output
<c>3</c>
### Example 8
#### Input
<c>"RBRBBRBRB"</c>
#### Output
<c>4</c>

"""
def findMaximumMatching(colors):
    return findMaximumMatchingHelper([c for c in colors])

def findMaximumMatchingHelper(colors):
    if len(colors) <= 1:
        return 0
    if colors[0] == colors[-1]:
        return 1 + findMaximumMatchingHelper(colors[1:-1])
    else:
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                return 1 + findMaximumMatchingHelper(colors[:i-1]+colors[i+1:])
        return (len(colors)-2) / 2

