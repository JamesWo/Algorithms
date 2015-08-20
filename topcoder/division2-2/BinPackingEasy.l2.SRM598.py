# srm 598 division 2 level 2
def minBins(item):
    item.sort()
    start = 0
    end = len(item)-1
    numPairs = 0
    while start < end:
        if item[start] + item[end] > 300:
            end -= 1
        else:
            start += 1
            end -= 1
            numPairs += 1
    return len(item) - numPairs
