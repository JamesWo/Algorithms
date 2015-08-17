maxType = 50

def getNumber(t):
    counts = {}
    for num in t:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    total = 0
    runningProduct = 1
    for i in range(1, maxType+2):
        if i not in counts:
            return total
        else:
            total += runningProduct * counts[i]
            runningProduct *= counts[i]
    assert False, "unreachable"

