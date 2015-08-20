"""
# [PiecewiseLinearFunctionDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15698&pm=12698)
*Single Round Match 586 Round 1 - Division II, Level Two*

## Statement
F is a function that is defined on all real numbers from the closed interval [1,N].
You are given a int[] *Y* with N elements.
For each i (1 <= i <= N) we have F(i) = *Y*[i-1].
Additionally, you know that F is piecewise linear: for each i, on the interval [i,i+1] F is a linear function.
The function F is uniquely determined by this information.
For example, if F(4)=1 and F(5)=6 then we must have F(4.7)=4.5.

As another example, this is the plot of the function F for *Y* = {1, 4, -1, 2}.

![image](images/2zecd35.png)

You are also given a int[] *query*.
For each i, compute the number of solutions to the equation F(x) = *query*[i].
Note that sometimes this number of solutions can be infinite.

Return a int[] of the same length as *query*.
For each i, element i of the return value should be -1 if the equation F(x) = *query*[i] has an infinite number of solutions.
Otherwise, element i of the return value should be the actual number of solutions this equation has.

## Definitions
- *Class*: `PiecewiseLinearFunctionDiv2`
- *Method*: `countSolutions`
- *Parameters*: `int[], int[]`
- *Returns*: `int[]`
- *Method signature*: `int[] countSolutions(int[] Y, int[] query)`

## Constraints
- *Y* will contain between 2 and 50 elements, inclusive.
- Each element of *Y* will be between -1,000,000,000 and 1,000,000,000, inclusive.
- *query* will contain between 1 and 50 elements, inclusive.
- Each element of *query* will be between -1,000,000,000 and 1,000,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>[1, 4, -1, 2],<br />[-2, -1, 0, 1]</c>
#### Output
<c>[0, 1, 2, 3 ]</c>
#### Reason
This is the example from the problem statement. The detailed information about the queries is:
There is no such x that F(x) = -2 is satisfied.
F(x) = -1 is only true for x = 3.
F(x) = 0 has two roots: 2.8 and 10/3.
F(x) = 1 has three roots: 1, 2.6 and 11/3.

### Example 2
#### Input
<c>[0, 0],<br />[-1, 0, 1]</c>
#### Output
<c>[0, -1, 0 ]</c>
#### Reason
This function's plot is a horizontal segment between points (1, 0) and (2, 0). F(x) = 0 is satisfied for any x between 1 and 2 and thus the number of solutions is infinite. For any other value on the right-hand side, it has no solutions.

### Example 3
#### Input
<c>[2, 4, 8, 0, 3, -6, 10],<br />[0, 1, 2, 3, 4, 0, 65536]</c>
#### Output
<c>[3, 4, 5, 4, 3, 3, 0 ]</c>
### Example 4
#### Input
<c>[-178080289, -771314989, -237251715, -949949900, -437883156, -835236871, -316363230, -929746634, -671700962],<br />[-673197622, -437883156, -251072978, 221380900, -771314989, -949949900, -910604034, -671700962, -929746634, -316363230]</c>
#### Output
<c>[8, 6, 3, 0, 7, 1, 4, 8, 3, 4 ]</c>

"""
def solve( Y, i ):
    count = 0
    for j in range( len(Y)-1 ):
        if Y[j] == i == Y[j+1]:
            return -1
        if (Y[j] <= i <= Y[j+1]) or (Y[j] >= i >= Y[j+1]):
            count += 1
    for elem in Y[1:-1]:
        if elem == i:
            count -= 1
    return count

def countSolutions(Y, query):
    result = []
    for i in query:
        s = solve( Y, i )
        result.append( s )
    return result
