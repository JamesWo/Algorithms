"""
Problem Statement

"You almost got us killed. Are you brainless?"

"I spake."

"The ability to speak does not make you intelligent. Now get out of here."

―Qui-Gon Jinn and Jar Jar Binks



Jar Jar Binks is the most clumsy character you will come across in Star Wars. He frequently gets into trouble because of this. Recently he went to a shoe store to buy a new pair of shoes. Unfortunately, as he entered the store, he tripped and fell on a rack of shoes.

The owner of the store is not happy to find Jar Jar binks at the bottom of a big heap of shoes, espcially since he had set fire to his shop last time he came around. The heap of shoes needs to be arranged into pairs.

Given a description of several shoes, you have to help Jar Jar Binks find the maximum number of pairs of shoes that can be formed.

Two shoes can form a pair only if their description is identical, except for the Type. The type of one shoe should be L (Left) and other should be R (Right).

Input Format

The first line contains N, the number of shoes.

Each of the next N lines contain description of a shoe in the form:

Companyi Sizei Colori Typei
Constraints:

1<=N<=1000
1<=|Companyi|<=20
1<=|Colori|<=20
0<=Sizei<=15
Companyi is a string of characters a-z
Colori is a string of characters a-z
Typei is either L, or R, indicating Left shoe and Right shoe respectively.
Output Format

Output a single integer: the number of pairs of shoes that can be made.
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
left = Counter()
right = Counter()
n = input()

for _ in range(n):
    s = raw_input()
    shoe = s[:-2]
    if s[-1] == 'L':
        left[shoe] += 1
    else:
        right[shoe] += 1
total = 0

for shoe in left:
    if shoe in right:
        total += min(left[shoe], right[shoe])
print total



