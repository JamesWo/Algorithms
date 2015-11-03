# given a sorted array with two elements swapped, find and fix the two elements swapped
# so that the array is sorted.

def fixSwapped(arr):
    # find first element that is lower than the previous
    assert len(arr) >= 2
    i = 1
    firstSwappedIndex = None
    while i < len(arr):
        if arr[i] < arr[i-1]:
            firstSwappedIndex = i - 1
            while firstSwappedIndex > 0 and \
                    arr[firstSwappedIndex] == arr[firstSwappedIndex-1]:
                firstSwappedIndex -= 1
            break
        i += 1
    else:
        #array is already sorted
        return
    
    i = len(arr)-1
    while i > 0 :
        if arr[i] < arr[i-1]:
            secondSwappedIndex = i
            while secondSwappedIndex < len(arr)-1 and \
                    arr[secondSwappedIndex] == arr[secondSwappedIndex+1]:
                secondSwappedIndex += 1
            break
        i -= 1
    tmp = arr[firstSwappedIndex]
    arr[firstSwappedIndex] = arr[secondSwappedIndex]
    arr[secondSwappedIndex] = tmp
    return





# test
import random
NUMBER_RANGE = 1000
ARR_LEN = 1000
NUM_CASES = 1000
for i in range(NUM_CASES):
    arr = [random.randint(-NUMBER_RANGE, NUMBER_RANGE) for _ in range(ARR_LEN)]
    arr.sort()
    index0 = random.randint(0, ARR_LEN-1)
    index1 = random.randint(0, ARR_LEN-1)
    tmp = arr[index0]
    arr[index0] = arr[index1]
    arr[index1] = tmp
    fixSwapped(arr)
    assert arr == sorted(arr), arr
