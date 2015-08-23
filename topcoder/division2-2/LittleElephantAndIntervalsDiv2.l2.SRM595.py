"""
# [LittleElephantAndIntervalsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15707&pm=12823)
*Single Round Match 595 Round 1 - Division II, Level Two*

## Statement
Little Elephant from the Zoo of Lviv has some balls arranged in a row. Each ball can be painted in one of two possible colors: black or white. Initially all the balls are painted white.

You are given an int *M*, which represents the number of balls in the row. 
The balls are numbered from left to right, starting from 1. 
You are also given two int[]s *L* and *R*. 
To repaint balls, Little Elephant wants to use a robot. 
The robot will paint the balls in several consecutive stages.
For each i, the i-th stage (1-based index) will look as follows:
First, the robot will choose one of the two colors: white or black.
Then, the robot will paint the balls with indices from *L*[i-1] to *R*[i-1], inclusive, using the chosen color.
(Painting a ball covers all previous layers of paint.)

Return the number of different colorings Little Elephant can get after the last stage. (Two colorings are considered different if there exists some ball that is white in one coloring and black in the other one).

## Definitions
- *Class*: `LittleElephantAndIntervalsDiv2`
- *Method*: `getNumber`
- *Parameters*: `int, int[], int[]`
- *Returns*: `int`
- *Method signature*: `int getNumber(int M, int[] L, int[] R)`

## Constraints
- *M* will be between 1 and 100, inclusive.
- *L* will contain between 1 and 10 elements, inclusive.
- *R* will contain the same number of elements as *L*.
- Each element of *R* will be between 1 and *M*, inclusive.
- i-th element of *L* will be between 1 and *R*[i], inclusive.

## Examples
### Example 1
#### Input
<c>4,<br />[1, 2, 3],<br />[1, 2, 3]</c>
#### Output
<c>8</c>
#### Reason
In the three stages the robot will choose the color for balls number 1, 2, and 3. The choices are independent of each other. The last, fourth ball will always remain white. Thus there are 2*2*2 = 8 different colorings.

### Example 2
#### Input
<c>3,<br />[1, 1, 2],<br />[3, 1, 3]</c>
#### Output
<c>4</c>
#### Reason
In the first stage the robot colors all three balls. The color chosen for the first stage does not matter, because in the second stage the robot will repaint ball 1, and in the third stage it will repaint balls 2 and 3.

### Example 3
#### Input
<c>100,<br />[47],<br />[74]</c>
#### Output
<c>2</c>
### Example 4
#### Input
<c>100,<br />[10, 20, 50],<br />[20, 50, 100]</c>
#### Output
<c>8</c>
### Example 5
#### Input
<c>42,<br />[5, 23, 4, 1, 15, 2, 22, 26, 13, 16],<br />[30, 41, 17, 1, 21, 6, 28, 30, 15, 19]</c>
#### Output
<c>512</c>

"""
def getNumber(M, L, R):
    s = set()
    s.add( "W"*M )
    for i in range(len(L)):
        s2 = set()
        for elem in s:
            s2.add( elem[:L[i]-1] + "W"*(R[i]-L[i]+1) + elem[R[i]:] )
            s2.add( elem[:L[i]-1] + "B"*(R[i]-L[i]+1) + elem[R[i]:] )
        s = s2
    return len(s)
