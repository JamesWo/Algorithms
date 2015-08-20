"""
# [SpaceWarDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15502&pm=12605)
*Single Round Match 582 Round 1 - Division II, Level Two*

## Statement
Magical Girls are girls who have magical powers.
They fight against evil to protect the Earth.
Cosmic enemies have just attacked the Earth, and the Magical Girls are going to fight them.

You are given a int[] *magicalGirlStrength* that describes the Magical Girls:
for each i, *magicalGirlStrength*[i] is the strength of one of the girls.
You are also given a int[] *enemyStrength* and a int[] *enemyCount* that describe their enemies:
for each i, there are *enemyCount*[i] enemies that each have strength *enemyStrength*[i].

Each Magical Girl will always fight one enemy at a time.
A Magical Girl will defeat her enemy if her strength is greater than or equal to the strength of that enemy.

At the beginning of the fight the fatigue of each Magical Girl is 0.
Each time a Magical Girl defeats an enemy, her fatigue increases by 1.

The Magical Girls want to defeat all the enemies.
That is, each of the enemies must be defeated by one of the Magical Girls.
Additionally, the Magical Girls want to minimize the maximum fatigue among them.

If it is impossible to defeat all of the enemies, return -1.
Otherwise, return the smallest F with the following property:
the Magical Girls can defeat all enemies in such a way that at the end the fatigue of each girl is at most F.

## Definitions
- *Class*: `SpaceWarDiv2`
- *Method*: `minimalFatigue`
- *Parameters*: `int[], int[], int[]`
- *Returns*: `int`
- *Method signature*: `int minimalFatigue(int[] magicalGirlStrength, int[] enemyStrength, int[] enemyCount)`

## Notes
- The elements of *enemyStrength* are not necessarily pairwise distinct.

## Constraints
- *magicalGirlStrength* will contain between 1 and 50 elements, inclusive.
- Each element of *magicalGirlStrength* will be between 1 and 100, inclusive.
- *enemyStrength* and *enemyCount* will each contain between 1 and 50 elements, inclusive.
- *enemyStrength* and *enemyCount* will contain the same number of elements.
- Each element of *enemyStrength* will be between 1 and 100, inclusive.
- Each element of *enemyCount* will be between 1 and 100, inclusive.

## Examples
### Example 1
#### Input
<c>[2, 3, 5],<br />[1, 3, 4],<br />[2, 9, 4]</c>
#### Output
<c>7</c>
#### Reason
There are 3 Magical Girls, their strength are 2, 3, and 5.
There are 3 kinds of enemies: 2 enemies with strength 1 each, 9 enemies with strength 3 each, and 4 enemies with strength 4 each. 

This is one of the ways how to minimize the maximal fatigue:
Magical girl 0 defeats 2 enemies with strength 1.
Magical girl 1 defeats 7 enemies with strength 3.
Magical girl 2 defeats 2 enemies with strength 3 and 4 enemies with strength 4.

### Example 2
#### Input
<c>[2, 3, 5],<br />[1, 1, 2],<br />[2, 9, 4]</c>
#### Output
<c>5</c>
#### Reason
Each of the Magical Girls can defeat any of the enemies. The optimal strategy is that each girl should defeat 5 of the enemies.

### Example 3
#### Input
<c>[14, 6, 22],<br />[8, 33],<br />[9, 1]</c>
#### Output
<c>-1</c>
#### Reason
None of the magical girls can beat the enemy with strength 33.

### Example 4
#### Input
<c>[17, 10, 29, 48, 92, 60, 80, 100, 15, 69, 36, 43, 70, 14, 88, 12, 14, 29, 9, 40],<br />[93, 59, 27, 68, 48, 82, 15, 95, 61, 49, 68, 15, 16, 26, 64, 82, 7, 8, 92, 15],<br />[56, 26, 12, 52, 5, 19, 93, 36, 69, 61, 68, 66, 55, 28, 49, 55, 63, 57, 33, 45]</c>
#### Output
<c>92</c>

"""
from bisect import bisect_left

def possible( i, arr ):
    sendLater = 0
    for j in range(len(arr)):
        if arr[j] > i:
            sendLater += ( arr[j] - i )
        elif arr[j] < i:
            free = ( i - arr[j] )
            subt =min( free, sendLater )
            sendLater -= subt
    if sendLater > 0:
        return False
    else:
        return True


def balance( arr ):
    for i in range( 0, 10001 ):
        if possible( i, arr[:] ):
            return i

def fastBalance( arr ):
    lo = 0
    hi = 10001
    while lo < hi:
        mid = ( lo + ( hi - lo ) / 2 )
        if possible( mid, arr[:] ):
            hi = mid
        else:
            lo = mid + 1
    return lo

def minimalFatigue(magicalGirlStrength, enemyStrength, enemyCount):
    magicalGirlStrength.sort()
    counts = [ 0 ] * len(magicalGirlStrength)
    for i in range( len( enemyCount ) ):
        ct = enemyCount[ i ]
        st = enemyStrength[ i ]
        index = bisect_left( magicalGirlStrength, st )
        if index >= len(counts):
            return -1
        counts[ index ] += ct
    return fastBalance( counts )


