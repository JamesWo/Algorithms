"""
# [LCMSetEasy](http://community.topcoder.com/tc?module=ProblemDetail&rd=15844&pm=13040)
*Single Round Match 611 Round 1 - Division II, Level Two*

## Statement
For any non-empty sequence of positive integers s1, s2, ..., sK their least common multiple is the smallest positive integer that is divisible by each of the given numbers.
We will use "lcm" to denote the least common multiple.
For example, lcm(3) = 3, lcm(4,6) = 12, and lcm(2,5,7) = 70.

You are given a int[] *S* and an int *x*.
Find out whether we can select some elements from *S* in such a way that their least common multiple will be precisely *x*.
Formally, we are looking for some s1, s2, ..., sK, K >= 1, such that each si belongs to *S*, and *x*=lcm(s1, s2, ..., sK).
Return "Possible" if such elements of *S* exist, and "Impossible" if they don't.

## Definitions
- *Class*: `LCMSetEasy`
- *Method*: `include`
- *Parameters*: `int[], int`
- *Returns*: `String`
- *Method signature*: `String include(int[] S, int x)`

## Constraints
- *S* will contain between 1 and 50 elements, inclusive.
- Each element in *S* will be between 1 and 1,000,000,000, inclusive.
- Elements in *S* will be distinct.
- *x* will be between 2 and 1,000,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>[2,3,4,5],<br />20</c>
#### Output
<c>"Possible"</c>
#### Reason
We can obtain 20 in multiple ways. One of them: 20 = lcm(4, 5).

### Example 2
#### Input
<c>[2,3,4],<br />611</c>
#### Output
<c>"Impossible"</c>
#### Reason
If *S*={2,3,4}, the only values we can obtain are 2, 3, 4, 6, and 12.

### Example 3
#### Input
<c>[2,3,4],<br />12</c>
#### Output
<c>"Possible"</c>
### Example 4
#### Input
<c>[1,2,3,4,5,6,7,8,9,10],<br />24</c>
#### Output
<c>"Possible"</c>
### Example 5
#### Input
<c>[100,200,300,400,500,600],<br />2000</c>
#### Output
<c>"Possible"</c>
### Example 6
#### Input
<c>[100,200,300,400,500,600],<br />8000</c>
#### Output
<c>"Impossible"</c>
### Example 7
#### Input
<c>[1000000000,999999999,999999998],<br />999999999</c>
#### Output
<c>"Possible"</c>
"""
def gcd(a, b):
    # base case
    if b < 1:
        return a
    #a, b = b, a % b
    tmp = b
    b = a % b
    a = tmp
    return gcd(a, b)

def lcm(a, b):
    return  a*b / gcd(a, b)

def include(S, x):
    divisors = []
    for elem in S:
        if x % elem == 0:
            divisors.append( elem )
    if not divisors:
        return "Impossible"
    # find gcd of all divisors
    lcmDiv = reduce( lcm, divisors )
    if lcmDiv == x:
        return "Possible"
    else:
        return "Impossible"




"""
Removing an element can only increase the gdc, thus decreasing the lcm.
Proof:  Assume L = lcm(S).  Consider S' a subset of S.  Then L divides
all elements of S' since L divides all elements of S.  Thus L is a 
common multiple of S', so lcm(S') <= L.

Let S be the set of all divisors of X in the original list.  Let 
L = lcm(S).  If L == X, then S is one solution.  
Claim:  If L != X, then there is no solution.
Proof:  If L < X, then any subset of S can only have a lower lcm,
        thus no subset of S can have lcm == X.
        L cannot be > X, since L is the least common multiple of S,
        and X is a common multiple of S.  

"""


















