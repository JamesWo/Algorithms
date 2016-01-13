#https://www.hackerrank.com/challenges/stockmax

def solve(prices):
    maxInLeft = [0] * len(prices)
    maxElem = 0
    for i in range(len(maxInLeft)-1, -1, -1):
        maxInLeft[i] = maxElem
        maxElem = max(maxElem, prices[i])
    money = 0
    numShares = 0
    for i in range(len(prices)):
        if maxInLeft[i] > prices[i]:
            numShares += 1
            money -= prices[i]
        else:
            money += numShares * prices[i]
            numShares = 0
    return money

numCases = input()
for _ in range(numCases):
    n = input()
    prices = map(int, raw_input().split(" "))
    print solve(prices)
