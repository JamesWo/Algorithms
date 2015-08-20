"""
# [GUMIAndSongsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15700&pm=12707)
*Single Round Match 588 Round 1 - Division II, Level Two*

## Statement
Gumi loves singing.
She knows N songs.
The songs are numbered 0 through N-1.
She now has some time and she would love to sing as many different songs as possible. 

You are given a int[] *duration*.
For each i, *duration*[i] is the duration of song i in Gumi's time units. 

Gumi finds it difficult to sing songs with quite different tones consecutively.
You are given a int[] *tone* with the following meaning:
If Gumi wants to sing song y immediately after song x, she will need to spend |*tone*[x]-*tone*[y]| units of time resting between the two songs.
(Here, || denotes absolute value.) 

You are also given an int *T*.
Gumi has *T* units of time for singing.
She can start singing any song she knows immediately at the beginning of this time interval.
Compute the maximal number of different songs she can sing completely within the given time.

## Definitions
- *Class*: `GUMIAndSongsDiv2`
- *Method*: `maxSongs`
- *Parameters*: `int[], int[], int`
- *Returns*: `int`
- *Method signature*: `int maxSongs(int[] duration, int[] tone, int T)`

## Constraints
- *duration* and *tone* will each contain between 1 and 15 elements, inclusive.
- *duration* and *tone* will contain the same number of elements.
- Each element of *duration* will be between 1 and 100,000, inclusive.
- Each element of *tone* will be between 1 and 100,000, inclusive.
- *T* will be between 1 and 10,000,000, inclusive.

## Examples
### Example 1
#### Input
<c>[3, 5, 4, 11],<br />[2, 1, 3, 1],<br />17</c>
#### Output
<c>3</c>
#### Reason
There are four songs. 
Two songs have tone 1 and their durations are 5 and 11, respectively.
One song has tone 2 and its duration is 3.
One song has tone 3 and its duration is 4.
Gumi has 17 units of time to sing. 

It is impossible for Gumi to sing all four songs she knows within the given time: even without the breaks the total length of all songs exceeds 17. 

Here is one way how she can sing three songs:
First, she sings song 0 in 3 units of time.
Second, she waits for |2-3|=1 unit of time and then sings song 2 in 4 units of time.
Finally, she waits for |3-1|=2 units of time and then sings song 1 in 5 units of time.
The total time spent is 3+1+4+2+5 = 15 units of time.

### Example 2
#### Input
<c>[100, 200, 300],<br />[1, 2, 3],<br />10</c>
#### Output
<c>0</c>
#### Reason
In this case, *T* is so small that she can't sing at all.

### Example 3
#### Input
<c>[1, 2, 3, 4],<br />[1, 1, 1, 1],<br />100</c>
#### Output
<c>4</c>
#### Reason
There is plenty of time, so she can sing all 4 songs.

### Example 4
#### Input
<c>[10, 10, 10],<br />[58, 58, 58],<br />30</c>
#### Output
<c>3</c>
### Example 5
#### Input
<c>[8, 11, 7, 15, 9, 16, 7, 9],<br />[3, 8, 5, 4, 2, 7, 4, 1],<br />14</c>
#### Output
<c>1</c>
### Example 6
#### Input
<c>[5611,39996,20200,56574,81643,90131,33486,99568,48112,97168,5600,49145,73590,3979,94614],<br />[2916,53353,64924,86481,44803,61254,99393,5993,40781,2174,67458,74263,69710,40044,80853],<br />302606</c>
#### Output
<c>8</c>

"""
import itertools
def possible( i, T, z):
    for songs in itertools.combinations( z, i ):
        songs = list(songs)
        songs.sort( key=lambda x:x[1] )
        totalTime = 0
        for j in range(1,len(songs)):
            totalTime += songs[j][1] - songs[j-1][1]
        totalTime += sum( map( lambda x:x[0], songs ) )
        if totalTime <= T:
            return True
    return False

def maxSongs(duration, tone, T):
    z = zip( duration, tone )
    for i in range(len(z),-1,-1):
        if possible(i, T, z):
            return i
    assert False
