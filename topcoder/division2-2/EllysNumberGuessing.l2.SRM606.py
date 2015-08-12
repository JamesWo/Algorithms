"""
# [EllysNumberGuessing](http://community.topcoder.com/tc?module=ProblemDetail&rd=15839&pm=12975)
*Single Round Match 606 Round 1 - Division I, Level One*

## Statement
Elly and Kris play the following game. In the beginning Kristina thinks of a number between 1 and 1,000,000,000, inclusive. After that Elly starts trying to guess it. In each round she says a number and Kristina says what is the absolute difference between the number she has thought of, and the number Elly guessed. Now Elly wonders if the guesses she has already made are sufficient to uniquely determine Kristina's number.

You are given a int[] *guesses* and a int[] *answers* of the same length. For each valid i, in round i of the game (0-based index) Elly guessed the number *guesses*[i] and Kristina answered *answers*[i]. If Kristina's number can be uniquely determined, return that number. If there are multiple possibilities that are consistent with the current set of guesses and answers, return -1. If it can be shown that at some point Kristina has lied (some of her answers were inconsistent), return -2.

## Definitions
- *Class*: `EllysNumberGuessing`
- *Method*: `getNumber`
- *Parameters*: `int[], int[]`
- *Returns*: `int`
- *Method signature*: `int getNumber(int[] guesses, int[] answers)`

## Constraints
- *guesses* and *answers* will each contain between 1 and 50 elements, inclusive.
- *guesses* and *answers* will contain the same number of elements.
- Each element of *guesses* will be between 1 and 1,000,000,000, inclusive.
- Each element of *answers* will be between 1 and 999,999,999, inclusive.

## Examples
### Example 1
#### Input
<c>[600, 594],<br />[6, 12]</c>
#### Output
<c>606</c>
#### Reason
Apparently Kristina has thought of the number of this SRM.

### Example 2
#### Input
<c>[100, 50, 34, 40],<br />[58, 8, 8, 2]</c>
#### Output
<c>42</c>
#### Reason
It is not guaranteed that Elly has used a perfect strategy so far.

### Example 3
#### Input
<c>[500000, 600000, 700000],<br />[120013, 220013, 79987]</c>
#### Output
<c>-2</c>
#### Reason
The answers here are inconsistent. After the second guess we can conclude that the answer is below 500000. But the third one indicates that it is above 500000. Thus, Kristina is a liar and you should return -2.

### Example 4
#### Input
<c>[500000000],<br />[133742666]</c>
#### Output
<c>-1</c>
#### Reason
There are multiple possibilities here, thus you should return -1.

### Example 5
#### Input
<c>[76938260, 523164588, 14196746, 296286419, 535893832,<br /> 41243148, 364561227, 270003278, 472017422, 367932361,<br /> 395758413, 301278456, 186276934, 316343129, 336557549,<br /> 52536121, 98343562, 356769915, 89249181, 335191879],<br />[466274085, 20047757, 529015599, 246925926, 7318513,<br /> 501969197, 178651118, 273209067, 71194923, 175279984,<br /> 147453932, 241933889, 356935411, 226869216, 206654796,<br /> 490676224, 444868783, 186442430, 453963164, 208020466]</c>
#### Output
<c>543212345</c>
### Example 6
#### Input
<c>[42],<br />[42]</c>
#### Output
<c>84</c>
#### Reason
Don't forget that the number Kris has thought of must be between 1 and 1,000,000,000.

### Example 7
#### Input
<c>[999900000],<br />[100001]</c>
#### Output
<c>999799999</c>
#### Reason
Don't forget that the number Kris has thought of must be between 1 and 1,000,000,000.



"""
global possibles

def isPossible( guess, answer ):
    global possibles
    lo = guess - answer
    hi = guess + answer
    ret = False
    if lo >= 1:
        ret |= ( lo in possibles )
    if hi <= 1000000000:
        ret |= ( hi in possibles )
    return ret

def getNumber(guesses, answers):
    global possibles
    possibles = set()
    if ( guesses[0] - answers[0] ) >= 1:
        possibles.add( guesses[0] - answers[0] )
    if ( guesses[0] + answers[0] ) <= 1000000000:
        possibles.add( guesses[0] + answers[0] )
    for guess, answer in zip( guesses, answers )[ 1: ]:
        if not isPossible( guess, answer ):
            return -2
        lo = guess - answer
        hi = guess + answer
        if lo in possibles and hi in possibles:
            continue
        elif lo in possibles:
            possibles = set( [ lo ] )
        elif hi in possibles:
            possibles = set( [ hi ] )
        else:
            assert False, 'unreachable'
    if len(possibles) == 0:
        return -2
    if len(possibles) == 1:
        return possibles.pop()
    else:
        return -1
