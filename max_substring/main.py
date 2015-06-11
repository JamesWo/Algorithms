# problem:
# Find the sub-array with the maximum sum
# Input: array of integers
# Output: array of integers, a sub-array of the input array


def maxSubarray(array):
    if not array:
        return []
    runningSum = [0]*len(array)
    runningSum[0] = array[0]
    for i in range(len(array)-1):
        print i
        runningSum[i+1] = runningSum[i]+array[i]
    print runningSum

testArray = [ 1, 1, 1 ]
maxSubarray(testArray)

