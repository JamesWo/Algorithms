# Hackerrank week15 2015
# haunted house
# https://www.hackerrank.com/contests/w15/challenges/haunted-house

def solve(arr, n):
    maxnstart = max([a[0] for a in arr]+[n])
    maxnend = max([a[1] for a in arr]+[n])
    startPoints = { x:0 for x in range(maxnstart+1) }
    endPoints = { x:0 for x in range(maxnend+1) }
    count = 0
    for start, end in arr:
            startPoints[start]+=1
            endPoints[end]+=1
            if start <= 0:
                count += 1
    best = 1 if count > 0 else 0
    lastSatisfied = count
    for num in range(1, n+1):
        satisfied = lastSatisfied + startPoints[num] - endPoints[num-1]
        lastSatisfied = satisfied
        if satisfied >= num:
            best = num
    return best

n = input()
ranges = []
for _ in range(n):
    x, y = map(int, raw_input().split())
    x += 1
    y += 1
    ranges.append((x,y))
print solve(ranges, n)
