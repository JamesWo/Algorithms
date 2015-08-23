import itertools
import math

def getNumber(N, K):
    total = 0
    for perm in itertools.permutations(range(N)):
        magicNum = 0
        for i in range(len(perm)):
            magicNum += max( i+1, perm[i]+1 )
        if magicNum >= K:
            total += 1
    return total * math.factorial(N)
