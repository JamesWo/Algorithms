# https://www.hackerrank.com/challenges/counter-game

def whoWins(n):
    moves = 0
    while n > 1:
        # if n is power of 2
        if (n&(n-1)==0):
            # divide n by 2
            n >>= 1
        else:
            # subtract largest power of 2
            shifted = 0
            tmp = n
            while tmp > 1:
                tmp >>= 1
                shifted += 1
            n &= ((1<<shifted)-1)
        moves += 1
    return "Richard" if (moves%2==0) else "Louise"
        
numCases = input()
for _ in range(numCases):
    print whoWins(input())

