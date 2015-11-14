#timed practice
import random 

def binarySearch(arr, target):
    if not arr:
        return -1
    lo = 0
    hi = len(arr)-1
    while lo < hi:
        mid = lo + (hi-lo)/2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    if arr[lo] == target:
        return lo
    else:
        return -1

#test
def linearSearch(arr, target):
    assert sorted(arr) == arr
    if not arr or target not in arr:
        return -1
    index = 0
    while index < len(arr):
        if arr[index] == target:
            return index
        index += 1
    return -1

NUMCASES = 1000
RANGE = 100
for _ in range(NUMCASES):
    arr = [random.randint(-RANGE,RANGE) for _ in range(random.randint(10,1000))]
    arr.sort()
    target = random.randint(-RANGE, RANGE)
    assert binarySearch(arr, target) == linearSearch(arr, target)
