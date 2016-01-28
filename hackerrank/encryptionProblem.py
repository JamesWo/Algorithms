# https://www.hackerrank.com/challenges/encryption

import math
word = raw_input()
lowerBound = int(math.floor(math.sqrt(len(word))))
upperBound = int(math.ceil(math.sqrt(len(word))))
for rows in range(lowerBound, upperBound+1):
    for cols in range(rows, upperBound+1):
        if rows * cols >= len(word):
            break

for col in range(cols):
    colLetters = []
    for row in range(rows):
        position = row * cols + col
        if position >= len(word):
            continue
        colLetters.append(word[position])
    print "".join(colLetters),
