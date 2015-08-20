"""
# [BigFatInteger2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15711&pm=12870)
*Single Round Match 599 Round 1 - Division II, Level Two*

## Statement
This problem statement contains superscipts that may not display properly outside the applet.

You are given four ints *A*, *B*, *C* and *D*. Return "divisible" (quotes for clarity) if *A**B* is divisible by *C**D*. Return "not divisible" otherwise.

## Definitions
- *Class*: `BigFatInteger2`
- *Method*: `isDivisible`
- *Parameters*: `int, int, int, int`
- *Returns*: `String`
- *Method signature*: `String isDivisible(int A, int B, int C, int D)`

## Notes
- The return value is case-sensitive.
- Positive integer y divides a positive integer x if and only if there is a positive integer z such that y*z=x. In particular, for each positive integer x, both 1 and x divide x.

## Constraints
- *A*, *B*, *C* and *D* will each be between 1 and 1,000,000,000 (10^(9)), inclusive.

## Examples
### Example 1
#### Input
<c>6,<br />1,<br />2,<br />1</c>
#### Output
<c>"divisible"</c>
#### Reason
Here, *A**B* = 6^(1) = 6 and *C**D* = 2^(1) = 2. 6 is divisible by 2.

### Example 2
#### Input
<c>2,<br />1,<br />6,<br />1</c>
#### Output
<c>"not divisible"</c>
#### Reason
2 is not divisible by 6.

### Example 3
#### Input
<c>1000000000,<br />1000000000,<br />1000000000,<br />200000000</c>
#### Output
<c>"divisible"</c>
#### Reason
Now the numbers are huge, but we can see that *A**B* is divisible by *C**D* from the fact that *A*=*C* and *B*>*D*.

### Example 4
#### Input
<c>8,<br />100,<br />4,<br />200</c>
#### Output
<c>"not divisible"</c>
#### Reason
We can rewrite 8^(100) as (2^(3))^(100) = 2^(300).
Similarly, 4^(200) = (2^(2))^(200) = 2^(400).
Thus, 8^(100) is not divisible by 4^(200).

### Example 5
#### Input
<c>999999937,<br />1000000000,<br />999999929,<br />1</c>
#### Output
<c>"not divisible"</c>
#### Reason
Here *A* and *C* are distinct prime numbers, which means *A**B* cannot have *C* as its divisor.

### Example 6
#### Input
<c>2,<br />2,<br />4,<br />1</c>
#### Output
<c>"divisible"</c>

"""

def factorNum(n):
    """ returns a dict mapping factors with the number of occurances """
    factors = {}
    i = 2
    while i*i <= n:
        if n % i == 0:
            n /= i
            if i not in factors:
                factors[i] = 1
            else:
                factors[i] += 1
        else:
            i += 1
    if n > 1:
        #assert n not in factors, n
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return factors

def isDivisible(A, B, C, D):
    Afactors = factorNum(A)
    Cfactors = factorNum(C)
    for factor, n in Cfactors.iteritems():
        if factor not in Afactors or \
             ( ( n * D ) > Afactors[factor]*B ):
            return "not divisible"
    return "divisible"


