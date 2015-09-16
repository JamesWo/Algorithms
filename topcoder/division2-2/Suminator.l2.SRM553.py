"""
# [Suminator](http://community.topcoder.com/tc?module=ProblemDetail&rd=15175&pm=11354)
*Single Round Match 553 Round 1 - Division I, Level One*

## Statement
Suminator is a very limited programming language.
A program in this language is simply a sequence of nonnegative integers.
The program is evaluated using a stack of nonnegative integers.
Initially, the stack is empty.
Trying to pop an element from an empty stack returns a zero.
(Alternately, you can imagine that the stack already contains a sufficient number of zeros in the beginning.)

A Suminator program is evaluated using the following algorithm:

for i = 0 to length(program) - 1 {
    if ( program[i] is 0) {
         Pop the top two elements from the stack, add them together
         and push the result to the top of the stack.
    } else {
         Push program[i] to the top of the stack.
    }
}
Pop the top element of the stack and print it.

For example, when executing the program {1}, we first push the 1 to the stack, and then we print it. 
When executing the program {5,0,1,2,0}, we take the following steps:
We push the 5 to the top of the stack.
We pop the top two elements (5 and 0), add them together and push the result (5).
We push the 1 to the top of the stack.
We push the 2 to the top of the stack. At this moment, the stack contains the values 5, 1, and 2 (from bottom to top).
We pop the top two elements (2 and 1), add them together and push the result (3).
We print the top element of the stack: the number 3. Note that the stack also contains the value 5, which is ignored.

You are given a int[] *program* containing a Suminator program (a sequence of nonnegative integers), in which one of the elements of the sequence was changed to -1.
You are also given a int *wantedResult*.
Your task is to change the -1 back to a nonnegative integer X in such a way that the resulting program prints the number *wantedResult*.
Return X.
If there are multiple possible values of X, return the smallest one.
If there is no way to make the program print *wantedResult*, return -1 instead.

## Definitions
- *Class*: `Suminator`
- *Method*: `findMissing`
- *Parameters*: `int[], int`
- *Returns*: `int`
- *Method signature*: `int findMissing(int[] program, int wantedResult)`

## Notes
- The return value always fits into an int. This follows from the constraints and the nature of the problem.

## Constraints
- *program* will contain between 1 and 50 elements, inclusive.
- Each element of *program* will be between -1 and 1000000000 (10^9), inclusive.
- *program* will contain -1 exactly once.
- *wantedResult* will be between 1 and 1000000000 (10^9), inclusive.

## Examples
### Example 1
#### Input
<c>[7,-1,0],<br />10</c>
#### Output
<c>3</c>
### Example 2
#### Input
<c>[100, 200, 300, 0, 100, -1],<br />600</c>
#### Output
<c>0</c>
### Example 3
#### Input
<c>[-1, 7, 3, 0, 1, 2, 0, 0],<br />13</c>
#### Output
<c>0</c>
#### Reason
We can replace the first element with many other values, but 0 is the smallest that achieves the wanted result.

### Example 4
#### Input
<c>[-1, 8, 4, 0, 1, 2, 0, 0],<br />16</c>
#### Output
<c>-1</c>
#### Reason
It does not matter what value we use in the first element of the array, the result will always be 15.

### Example 5
#### Input
<c>[1000000000, 1000000000, 1000000000,  1000000000, -1, 0, 0, 0, 0],<br />1000000000</c>
#### Output
<c>-1</c>
#### Reason
It does not matter what we replace the -1 with, the result will be larger than 1000000000.

### Example 6
#### Input
<c>[7, -1, 3, 0],<br />3</c>
#### Output
<c>-1</c>

"""
def runProgram(program):
    """
    for i = 0 to length(program) - 1 {
        if ( program[i] is 0) {
             Pop the top two elements from the stack, add them together
            and push the result to the top of the stack.
        } else {
             Push program[i] to the top of the stack.
        }
    }
    """
    stack = [0]*(len(program)+1)
    for i in program:
        if i == 0:
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(i)
    return stack.pop()

def findMissing(program, wantedResult):
    assert program.count( -1 ) == 1
    missing = program.index(-1)
    program[missing] = 0
    if runProgram(program) == wantedResult:
        return 0
    lo = 1
    # here I make the assumption that -1 was originally
    # a number between 0 and 10**9, like all the other numbers
    hi = 10**9
    while lo < hi:
        mid = lo + (hi-lo)/2
        program[missing] = mid
        result = runProgram(program)
        if result < wantedResult:
            lo = mid + 1
        else:
            hi = mid
    assert lo == hi
    program[missing] = lo
    if runProgram(program) == wantedResult:
        return lo
    else:
        return -1
