"""
# [EmoticonsDiv2](http://community.topcoder.com/tc?module=ProblemDetail&rd=15845&pm=13041)
*Single Round Match 612 Round 1 - Division II, Level Two*

## Statement
You are very happy because you advanced to the next round of a very important programming contest.
You want your best friend to know how happy you are.
Therefore, you are going to send him a lot of smile emoticons.
You are given an int *smiles*: the exact number of emoticons you want to send.

You have already typed one emoticon into the chat.
Then, you realized that typing is slow.
Instead, you will produce the remaining emoticons using copy and paste.

You can only do two different operations:
Copy all the emoticons you currently have into the clipboard.
Paste all emoticons from the clipboard.
Each operation takes precisely one second.
Copying replaces the old content of the clipboard.
Pasting does not empty the clipboard.
Note that you are not allowed to copy just a part of the emoticons you already have.

Return the smallest number of seconds in which you can turn the one initial emoticon into *smiles* emoticons.

## Definitions
- *Class*: `EmoticonsDiv2`
- *Method*: `printSmiles`
- *Parameters*: `int`
- *Returns*: `int`
- *Method signature*: `int printSmiles(int smiles)`

## Constraints
- *smiles* will be between 2 and 1000, inclusive.

## Examples
### Example 1
#### Input
<c>2</c>
#### Output
<c>2</c>
#### Reason
First use copy, then use paste. The first operation copies one emoticon into the clipboard, the second operation pastes it into the message, so now you have two emoticons and you are done.

### Example 2
#### Input
<c>6</c>
#### Output
<c>5</c>
#### Reason
Copy. This puts one emoticon into the clipboard.
Paste. You now have 2 emoticons in the message.
Copy. The clipboard now contains 2 emoticons.
Paste. You now have 4 emoticons in the message.
Paste. You now have 6 emoticons in the message and you are done.

### Example 3
#### Input
<c>11</c>
#### Output
<c>11</c>
### Example 4
#### Input
<c>16</c>
#### Output
<c>8</c>
### Example 5
#### Input
<c>1000</c>
#### Output
<c>21</c>
"""

"""
The optimal solution is equivalent to the sum of the prime factors of n.

Proof:
If you start with K smiles, you can reach any multiple of K, d*K for d >= 2, in exactly d time,
since you copy K once, then paste (d-1) times.

Consider the sequence [ X1, X2, X3 ... XN ], denoting the multiples taken starting from 1.
You start at 1, go to 1*X1, then to go 1*X1*X2, then to 1*X1*X2*X3, and so on.
Then the time taken is the sum of X1 + X2 + ... XN.

Thus this problem simplies to finding a sequence of integers X1 ... XN such that the
product of X1 ... XN == smiles.  We want to minimize the sum of this sequence.  

Notice that by definition, each Xi is a divisor of smiles.
Assume some integer Xi in this sequence is not prime.  
Then splitting up Xi into two proper divisors will create a new sequence with
a lower or equivalent sum.  ( lemma 1 )

lemma 1: Assume A>1, B>1.  If A * B == D, then A + B <= D.  
Proof:
    D
    = A * B 
    = ( (A-1) * B ) + B
    = ( (A-1) * (B-1) ) + (A-1) + B
    <= ( 1 ) + ( A - 1 ) + B    # since (A-1) >= 1 and (B-1) >= 1
    = A + B
"""

def divisors(n):
    i = 2
    while i <= n:
	if n % i == 0:
	    yield(i)
	i += 1

global answers

def printSmiles1(smiles):
    global answers
    answers = [ -1 for _ in range(smiles+1) ]
    answers[1] = 0
    return printSmiles1_(smiles)

def printSmiles1_(smiles):
    global answers
    if answers[smiles] != -1:
	return answers[smiles]
    best = smiles+1
    for d in divisors( smiles ):
	cost = printSmiles1_( smiles/d )
	cost += 1 # copy it
	cost += ( d - 1 ) # paste it d-1 times
	best = min( best, cost )
    answers[smiles] = best
    return best

def printSmiles2(smiles):
    total = 0
    i = 2
    while i**2 <= smiles:
	if smiles % i == 0:
	    total += i
	    smiles /= i
	else:
	    i += 1
    if smiles != 1:
	total += smiles
    return total

def printSmiles(smiles):
    return printSmiles2(smiles)

# run larger tests
print printSmiles( 2**64 -1 )






import pdb; pdb.set_trace()

