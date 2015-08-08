"""

# [ColorfulCoinsEasy](http://community.topcoder.com/tc?module=ProblemDetail&rd=15849&pm=13094)
*Single Round Match 616 Round 1 - Division II, Level Two*

## Statement
The currency system in Colorland consists of various types of coins. The coin denominations follow these simple rules:

The denominations are distinct positive integers.
There is a coin type with denomination 1.
For each pair of different coin types, the denomination of one coin type divides the denomination of the other one.

You are given a int[] *values* containing all the available denominations in ascending order.

Coins of different denominations look exactly the same except that they have different colors. Each coin in Colorland has exactly one color. The coin colors follow these even simpler rules:

All coins of the same type are of the same color.
No two coins of different types are of the same color.

You know all coin denominations used in Colorland, but you don't know their colors. You don't even know the set of colors used on the coins.

For each denomination, you'd like to know the color of coins of this denomination. To accomplish this, you've got a credit card with an infinite amount of money. You can perform a single query to an ATM which can also provide you with an infinite amount of money. The query is described by a positive integer X, which means that you want to receive exactly X units of money from the ATM. The ATM will provide you with the requested amount. You also know that the requested amount will be paid using the smallest possible number of coins. (Note that this rule always uniquely determines the set of coins chosen to make the payment.)

Return "Possible" (quotes for clarity) if it's possible to determine the color of coins of each denomination, and return "Impossible" otherwise.

## Definitions
- *Class*: `ColorfulCoinsEasy`
- *Method*: `isPossible`
- *Parameters*: `int[]`
- *Returns*: `String`
- *Method signature*: `String isPossible(int[] values)`

## Constraints
- *values* will contain between 1 and 15 elements, inclusive.
- Each element of *values* will be between 1 and 20000, inclusive.
- *values* will be sorted in strictly ascending order. Note that this also implies that all the elements of *values* will be distinct.
- For each pair of different elements in *values*, the smaller one will be a divisor of the larger one.
- *values*[0] will be 1.

## Examples
### Example 1
#### Input
<c>[1]</c>
#### Output
<c>"Possible"</c>
#### Reason
For any positive X, you'll get exactly X coins of denomination 1, so you'll easily learn their color.

### Example 2
#### Input
<c>[1, 3]</c>
#### Output
<c>"Possible"</c>
#### Reason
X = 5 is one possible solution. As the ATM gives the smallest number of coins, it will give one coin of denomination 3 and two coins of denomination 1. That means, for example, that if you get one red coin and two blue coins, you'll understand that coins of denomination 3 are red, and coins of denomination 1 are blue.

### Example 3
#### Input
<c>[1, 2, 4]</c>
#### Output
<c>"Impossible"</c>
#### Reason
It can be proven that for any X, you'll get at most one coin of denomination 1, and at most one coin of denomination 2. If you get no coins of some denomination, clearly you won't be able to determine their color. However, if you get one coin from each of denominations 1 and 2, you won't be able to find out which of the two colors represents which denomination.

### Example 4
#### Input
<c>[1, 5, 15, 90]</c>
#### Output
<c>"Possible"</c>
#### Reason
X = 504 is one possible solution. You'll get five coins of denomination 90, three coins of denomination 15, one coin of denomination 5 and four coins of denomination 1.

### Example 5
#### Input
<c>[1, 4, 20, 60, 180, 1440, 5760]</c>
#### Output
<c>"Impossible"</c>
### Example 6
#### Input
<c>[1, 7, 21, 105, 630, 3150, 18900]</c>
#### Output
<c>"Possible"</c>
#### Reason
X = 137969 is the smallest possible solution.

### Example 7
#### Input
<c>[1, 10, 30, 300, 900, 9000, 18000]</c>
#### Output
<c>"Impossible"</c>
### Example 8
#### Input
<c>[1, 2, 10, 40, 200, 1000, 4000, 20000]</c>
#### Output
<c>"Impossible"</c>
"""

def isPossibleHelper(values, i):
    counts = set([0])
    for value in values[::-1]:
        counts.add( i / value )
        i %= value
    return (len(counts)-1) == len(values)


def isPossible1(values):
    for i in range(20001*15):
        if isPossibleHelper(values, i):
            #print i
            return "Possible"
    return "Impossible"


def isPossible2(values):
    # attempt 2
    divisors = []
    for i in range(1, len(values)):
        divisors.append(( values[i] / values[i-1] ) - 1 )
    divisors.sort()
    for i in range(len(divisors)):
        if (i+1) > divisors[i]:
            return "Impossible"
    return "Possible"


def isPossible(values):
    return isPossible2(values)

