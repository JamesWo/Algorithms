"""
# [NumbersChallenge](http://community.topcoder.com/tc?module=ProblemDetail&rd=15854&pm=13166)
*Single Round Match 621 Round 1 - Division II, Level Two*

## Statement
Your friend Lucas gave you a sequence *S* of positive integers.

For a while, you two played a simple game with *S*:
Lucas would pick a number, and you had to select some elements of *S* such that the sum of all numbers you selected is the number chosen by Lucas.
For example, if *S*={2,1,2,7} and Lucas chose the number 11, you would answer that 2+2+7 = 11.

Lucas now wants to trick you by choosing a number X such that there will be no valid answer.
For example, if *S*={2,1,2,7}, it is not possible to select elements of *S* that sum up to 6.

You are given the int[] *S*.
Find the smallest positive integer X that cannot be obtained as the sum of some (possibly all) elements of *S*.

## Definitions
- *Class*: `NumbersChallenge`
- *Method*: `MinNumber`
- *Parameters*: `int[]`
- *Returns*: `int`
- *Method signature*: `int MinNumber(int[] S)`

## Constraints
- *S* will contain between 1 and 20 elements, inclusive.
- Each element of *S* will be between 1 and 100,000, inclusive.

## Examples
### Example 1
#### Input
<c>[5, 1, 2]</c>
#### Output
<c>4</c>
#### Reason
These are all the positive integers that can be obtained: 1, 2, 3, 5, 6, 7, and 8.
(We can obtain 3 as 1+2, 6 as 1+5, 7 as 2+5, and 8 as 1+2+5.)
The smallest positive integer not present in the above list is 4.

### Example 2
#### Input
<c>[2, 1, 4]</c>
#### Output
<c>8</c>
#### Reason
We can obtain each of the sums from 1 to 7, inclusive. The smallest impossible sum is 8.

### Example 3
#### Input
<c>[2, 1, 2, 7]</c>
#### Output
<c>6</c>
#### Reason
The example given in the problem statement.

### Example 4
#### Input
<c>[94512, 2, 87654, 81316, 6, 5, 6, 37151, 6, 139, 1, 36, 307, 1, 377, 101, 8, 37, 58, 1]</c>
#### Output
<c>1092</c>
### Example 5
#### Input
<c>[883, 66392, 3531, 28257, 1, 14131, 57, 1, 25, 88474, 4, 1, 110, 6, 1769, 220, 442, 7064, 7, 13]</c>
#### Output
<c>56523</c>
"""


import itertools

def possible1(S):
    ret = set()
    for bitmask in range((1 << (len(S)))):
        total = 0
        index = 0
        while bitmask:
            if ( bitmask & 1 ):
                total += S[index]
            bitmask >>= 1
            index += 1
        ret.add(total)
    return ret


def possible2(S):
    for k in range(1,len(S)+1):
        for comb in itertools.combinations(S, k):
            yield sum(comb)

def MinNumber1(S):
    # save that in a set:
    poss = set( possible2(S) )
    # first integer >= 1 that is not in the set:
    return next( x for x in itertools.count(1) if x not in poss )

    
def MinNumber2(S):
    possibleNums = set( possible2(S) )
    for i in range(1, 100000*20):
        if i not in possibleNums:
            return i

def MinNumber(S):
    return MinNumber2(S)
