"""
# [BearSortsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=16513&pm=13941)
*Single Round Match 664 Round 1 - Division II, Level Three*

## Statement
Bear Limak was chilling in the forest when he suddenly found a computer program.
The program was a correct implementation of MergeSort.
Below you can find the program in pseudocode.

# mergeSort(left,right) sorts elements left, left+1, ..., right-1 of a global array T
function mergeSort(left,right):
    # if there is at most one element, we are done
    if left+1 >= right: return

    # otherwise, split the sequence into halves, sort each half separately
    mid = (left + right) div 2
    mergeSort(left,mid)
    mergeSort(mid,right)

    # then merge the two halves together
    merged = []     # an empty sequence
    p1 = left
    p2 = mid
    while (p1 < mid) or (p2 < right):
        if p1 == mid:
            merged.append( T[p2] )
            p2 += 1
        else if p2 == right:
            merged.append( T[p1] )
            p1 += 1
        else:
            if LESS( T[p1], T[p2] ):
                merged.append( T[p1] )
                p1 += 1
            else:
                merged.append( T[p2] )
                p2 += 1

    # finally, move the merged elements back into the original array
    for i from left to right-1 inclusive:
        T[i] = merged[i-left]

Limak noticed that one part of the implementation was missing: the function LESS.
You can probably guess that the function is supposed to return a boolean value stating whether the first argument is less than the second argument.
However, Limak is a bear and he didn't know that.
Instead he implemented his own version of this function.
Limak's function uses a true random number generator.
Each of the two possible return values (true, false) is returned with probability 50 percent.

The random values generated in different calls to Limak's function LESS are mutually independent.
Note that even if you call LESS twice with the same arguments, the two return values may differ.

After implementing LESS, Limak decided to run his brand new program.
He initialized the global array T to contain N elements.
Then, he filled the values 1 through N into the array: for each valid i, he set T[i] to i+1.
Finally, he executed the function mergeSort(0,N).

Even with Limak's new LESS function, the program never crashes.
On the other hand, it does not necessarily produce a sorted sequence when it terminates.
In general, when the program terminates, the array T will contain some permutation of the numbers 1 through N.

After running the program many times, Limak has noticed that different output permutations are produced with different probabilities.
Your task is to help him learn more about these probabilities.
More precisely, your task is to compute the probability that a given sequence will appear as the output of Limak's program.

You are given a int[] *sortedSequence* with N elements, containing a permutation of 1 through N.
Let P be the probability that Limak's program, when run on an array with N elements, outputs this permutation.
Return the value log(P), where log denotes the natural (base e) logarithm.

## Definitions
- *Class*: `BearSortsDiv2`
- *Method*: `getProbability`
- *Parameters*: `int[]`
- *Returns*: `double`
- *Method signature*: `double getProbability(int[] seq)`

## Notes
- Your return value must have absolute or relative error smaller than 1e-9.
- You may assume that for each N and for each permutation P of 1 through N the probability that P appears as the output of Limak's program is strictly positive.

## Constraints
- *sortedSequence* will contain exactly N elements.
- N will be between 1 and 40, inclusive.
- Elements of *sortedSequence* will be between 1 and N, inclusive.
- Elements of *sortedSequence* will be pairwise distinct.

## Examples
### Example 1
#### Input
<c>[1,2]</c>
#### Output
<c>-0.6931471805599453</c>
#### Reason
Limak is sorting a 2-element sequence.
The algorithm will split it into two 1-element sequences and then it will merge those together.
While merging, the algorithm will call LESS(1, 2) to "compare" the two elements.
If LESS(1, 2) returns true, the resulting permutation will be {1, 2}, otherwise it will be {2, 1}.
Therefore, the probability of each of those two permutations is equal to 0.5.
The return value is log(0.5).

### Example 2
#### Input
<c>[1,3,2]</c>
#### Output
<c>-1.3862943611198906</c>
#### Reason
When {1, 2, 3} is sorted, it is first split into {1} and {2, 3}.
After that, in order to obtain {1, 3, 2} in the end, two things must happen, one after another:
When {2, 3} is recursively sorted, the result must be {3, 2}. From Example 0 we know this happens with probability 0.5.
When merging {1} and {3, 2}, the first call to LESS will be LESS(1, 3). This call must return true. Again, this happens with probability 0.5.
Therefore, the probability is 0.5 * 0.5 = 0.25, and the answer is log(0.25).

### Example 3
#### Input
<c>[10,13,18,2,4,6,24,22,19,5,7,20,23,14,21,17,25,3,1,11,12,8,15,16,9]</c>
#### Output
<c>-57.53121598647546</c>
"""

import math

global calls

# unused
def mergeSortCountCalls( seq, left, right ):
    global calls
    if left + 1 >= right:
        return
    mid = ( left + right ) / 2
    mergeSortCountCalls( seq, left, mid )
    mergeSortCountCalls( seq, mid, right )

    merged = []
    p1 = left
    p2 = mid
    while (p1 < mid) or (p2 < right):
        if p1 == mid:
            merged.append( seq[p2] )
            p2 += 1
        elif p2 == right:
            merged.append( seq[p1] )
            p1 += 1
        else:
            calls += 1
            if seq[p1] < seq[p2]:
                merged.append( seq[p1] )
                p1 += 1
            else:
                merged.append( seq[p2] )
                p2 += 1
    for i in range( left, right ):
        seq[i] = merged[ i-left ]

def comp( i, j, goal ):
    return goal.index(i) < goal.index(j)

def mergeSortBackwards( seq, goal, left, right ):
    global calls
    if left + 1 >= right:
        return
    mid = ( left + right ) / 2
    mergeSortBackwards( seq, goal, left, mid )
    mergeSortBackwards( seq, goal, mid, right )

    merged = []
    p1 = left
    p2 = mid
    while (p1 < mid) or (p2 < right):
        if p1 == mid:
            merged.append( seq[p2] )
            p2 += 1
        elif p2 == right:
            merged.append( seq[p1] )
            p1 += 1
        else:
            calls += 1
            if comp( seq[p1], seq[p2], goal ):
                merged.append( seq[p1] )
                p1 += 1
            else:
                merged.append( seq[p2] )
                p2 += 1
    for i in range( left, right ):
        seq[i] = merged[ i-left ]

def getProbability(seq):
    global calls
    calls = 0
    mergeSortBackwards( [ i for i in range(1, len(seq)+1) ], seq, 0, len(seq) )
    prob = 2 ** calls
    return math.log( 1.0 / float( prob ) )



