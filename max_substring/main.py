# problem:
# Find the sub-array with the maximum sum
# Input: array of integers
# Output: array of integers, a sub-array of the input array such that
# 1. the sum of the sub-array is maximal
# 2. the size of the sub-array is minimal

def maxSubarray(array):
    if not array:
        return []
    runningSum = [0]*len(array)
    runningSum[0] = array[0]
    min = runningSum[0]
    mini = 0
    tmpMin = runningSum[0]
    max = runningSum[0]
    maxi = 0
    for i in range(len(array)-1):
        runningSum[i+1] = runningSum[i]+array[i]
        if runningSum[i+1] > max:
            max = runningSum[i+1]
            maxi = i+1
        if runningSum[i+1] < min:
            min = runningSum[i+1]
            mini = i+1
    print runningSum
    print min, mini
    print max, maxi

    if array[mini] <= 0:
        array[mini] += 1
testArray = [ 1, 1, 1 ]
maxSubarray(testArray)

