"""
# [CuttingBitString](http://community.topcoder.com/tc?module=ProblemDetail&rd=15177&pm=12155)
*Single Round Match 555 Round 1 - Division I, Level One*

## Statement
We are in a distant future.
After the downfall of mankind, the Earth is now ruled by fairies.
The "Turing game Online" website is hot among fairies right now.
On this website, everyone can play the programming puzzle "Turing game".

Fairies love powers of 5, that is, the numbers 1, 5, 25, 125, 625, and so on.
In the Turing game, the player is given a string of bits (zeros and ones).
The ideal situation is when the string is represents a power of 5 in binary, with no leading zeros.
If that is not the case, the fairy player tries to cut the given string into pieces, each piece being a binary representation of a power of 5, with no leading zeros.
Of course, it may be the case that even this is impossible.
In that case, the fairy player becomes depressed, and bad things happen when a fairy gets depressed.
You, as one of the surviving humans, are in charge of checking the bit strings to prevent the bad things from happening.

You are given a String *S* that consists of characters '0' and '1' only.
*S* represents the string given to a player of the Turing game.
Return the smallest positive integer K such that it is possible to cut *S* into K pieces, each of them being a power of 5.
If there is no such K, return -1 instead.

## Definitions
- *Class*: `CuttingBitString`
- *Method*: `getmin`
- *Parameters*: `String`
- *Returns*: `int`
- *Method signature*: `int getmin(String S)`

## Constraints
- *S* will contain between 1 and 50 characters, inclusive.
- Each character in *S* will be either '0' or '1'.

## Examples
### Example 1
#### Input
<c>"101101101"</c>
#### Output
<c>3</c>
#### Reason
We can split the given string into three "101"s.

Note that "101" is 5 in binary.

### Example 2
#### Input
<c>"1111101"</c>
#### Output
<c>1</c>
#### Reason
"1111101" is 5^3.

### Example 3
#### Input
<c>"00000"</c>
#### Output
<c>-1</c>
#### Reason
0 is not a power of 5.

### Example 4
#### Input
<c>"110011011"</c>
#### Output
<c>3</c>
#### Reason
Split it into "11001", "101" and "1".

### Example 5
#### Input
<c>"1000101011"</c>
#### Output
<c>-1</c>
### Example 6
#### Input
<c>"111011100110101100101110111"</c>
#### Output
<c>5</c>

"""
def getmin(S):
    power = 1
    powersOf5 = set()
    while power.bit_length() <= 50:
        powersOf5.add(bin(power)[2:])
        power *= 5

    d = {}
    for sublen in range(1,len(S)+1):
        for startIndex in range(len(S)-sublen+1):
            endIndex = startIndex+sublen
            substr = S[startIndex:endIndex]
            if substr in powersOf5:
                d[(startIndex, endIndex)] = 1
            else:
                best = None
                for split in range(startIndex+1, endIndex):
                    left = (startIndex, split)
                    right = (split, endIndex)
                    if left not in d or right not in d:
                        continue
                    cost = d[left] + d[right]
                    if not best or best > cost:
                        best = cost
                if best:
                    d[(startIndex, endIndex)] = best
    if (0, len(S)) not in d:
        return -1
    return d[(0, len(S))]

    

