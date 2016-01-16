#https://www.hackerrank.com/challenges/board-cutting

def solve(m, n, mCosts, nCosts):
    combinedCosts = map(lambda cost:(cost, "m"), mCosts) + map(lambda cost:(cost, "n"), nCosts)
    combinedCosts.sort(key = lambda x:x[0], reverse=True)
    mSplits = 1
    nSplits = 1
    totalCost = 0
    for cost, position in combinedCosts:
        if position == 'm':
            mSplits += 1
            totalCost += (cost * nSplits)
        elif position == 'n':
            nSplits += 1
            totalCost += (cost * mSplits)
        else:
            assert False, "incorrect position"
    return totalCost    


numCases = input()
for _ in range(numCases):
    m, n = map(int, raw_input().split(" "))
    mCosts = map(int, raw_input().split(" "))
    nCosts = map(int, raw_input().split(" "))
    print solve(m, n, mCosts, nCosts)


