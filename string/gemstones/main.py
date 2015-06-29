#https://www.hackerrank.com/challenges/gem-stones
import string
numRocks = input()
rocks = []
for _ in range(numRocks):
    rocks.append(raw_input())
count = 0
for char in string.ascii_lowercase:
    for rock in rocks:
        if char not in rock:
            break
    else:
        count += 1
print count
