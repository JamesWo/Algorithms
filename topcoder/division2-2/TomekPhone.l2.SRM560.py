"""
# [TomekPhone](http://community.topcoder.com/tc?module=ProblemDetail&rd=15182&pm=12296)
*Single Round Match 560 Round 1 - Division I, Level One*

## Statement
Tomek thinks that smartphones are overrated.
He plans to release a new cellphone with an old-school keyboard, which may require you to tap a key multiple times to type a single letter.
For example, if the keyboard has two keys, one with the letters "adef" and the other one with the letters "zyx", then typing 'a' requires one keystroke, typing 'f' requires four keystrokes, typing 'y' requires two keystrokes, and so on.

Tomek has already designed the keyboard's layout.
That is, he already knows the number of keys on the keyboard, and for each key he knows the maximum number of letters it may hold.
He now wants to create a specific keyboard for a language that uses N different letters.
He has a large body of text in this language, and he already analyzed it to find the frequencies of all N letters of its alphabet.

You are given a int[] *frequencies* with N elements.
Each element of *frequencies* is the number of times one of the letters in Tomek's alphabet appears in the text he has.
Each element of *frequencies* will be strictly positive.
(I.e., each of the N letters occurs at least once in Tomek's text.)

You are also given a int[] *keySize*.
The number of elements of *keySize* is the number of keys on Tomek's keyboard.
Each element of *keySize* gives the maximal number of letters on one of the keys.

Find an assignment of letters to keys that minimizes the number of keystrokes needed to type Tomek's entire text.
Return that minimum number of keystrokes.
If there is not enough room on the keys and some letters of the alphabet won't fit, return -1 instead.

## Definitions
- *Class*: `TomekPhone`
- *Method*: `minKeystrokes`
- *Parameters*: `int[], int[]`
- *Returns*: `int`
- *Method signature*: `int minKeystrokes(int[] frequencies, int[] keySizes)`

## Constraints
- *frequencies* will contain between 1 and 50 elements, inclusive.
- Each element of *frequencies* will be between 1 and 1,000, inclusive.
- *keySizes* will contain between 1 and 50 elements, inclusive.
- Each element of *keySizes* will be between 1 and 50, inclusive.

## Examples
### Example 1
#### Input
<c>[7,3,4,1],<br />[2,2]</c>
#### Output
<c>19</c>
#### Reason
Tomek's language has four letters.
Let us call them A, B, C, and D.
Tomek's text contains seven As, three Bs, four Cs, and one D.
The keyboard has two keys, each of them may contain at most two letters.
One optimal solution is to use the keys "AD" and "CB".
We can then type each A and each C using a single keystroke, and we need two keystrokes for each B and each D.
Therefore, the total number of keystrokes when typing the entire text will be 7*1 + 3*2 + 4*1 + 1*2 = 19.

### Example 2
#### Input
<c>[13,7,4,20],<br />[2,1]</c>
#### Output
<c>-1</c>
#### Reason
There is not enough space on the keys to fit all four letters.

### Example 3
#### Input
<c>[11,23,4,50,1000,7,18],<br />[3,1,4]</c>
#### Output
<c>1164</c>
### Example 4
#### Input
<c>[100,1000,1,10],<br />[50]</c>
#### Output
<c>1234</c>
### Example 5
#### Input
<c>[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],<br />[10,10,10,10,10,10,10,10]</c>
#### Output
<c>3353</c>

"""
def minKeystrokes(frequencies, keySizes):
    total = 0
    keys = [[0,i] for i in keySizes if i != 0]
    for i in sorted(frequencies, reverse=True):
        if not keys:
            return -1
        used = map(lambda x:x[0], keys)
        minIndex = used.index(min(used))
        keys[minIndex][0] += 1
        total += keys[minIndex][0]*i
        if keys[minIndex][0] == keys[minIndex][1]:
            keys = keys[:minIndex]+keys[minIndex+1:]
    return total
