# problem:
# Find the sub-array with the maximum sum
# Input: array of integers
# Output: array of integers, a sub-array of the input array such that
# 1. the sum of the sub-array is maximal
# 2. the size of the sub-array is minimal

__debugMode = False
def log(*args):
    if __debugMode:
        for arg in args:
            print(str(arg))

def maxSubarray(array):
    if not array:
        return []
    if not isinstance(array, type([])):
        return []
    runningSum = [0]*len(array)
    runningSum[0] = array[0]
    min = runningSum[0]
    mini = 0
    tmpMin = runningSum[0]
    tmpMini = 0
    max = runningSum[0]
    maxi = 0
    for i in range(1, len(array)):
        #print i
        runningSum[i] = runningSum[i-1]+array[i]
        if runningSum[i] > max:
            max = runningSum[i]
            maxi = i
            min = tmpMin
            mini = tmpMini
        if runningSum[i] <= tmpMin:
            tmpMin = runningSum[i]
            tmpMini = i

    log(runningSum)
    log(mini, maxi)
    
    if array[mini] <= 0:
        mini += 1
    log(mini, maxi)
    if runningSum[mini] > 0:
        found=False
        # We want mini to be the smallest i such that everything up to i sum to 0
        for i in range(0, mini):
            if runningSum[i] == 0:
                mini2 = i+1
                found=True
        if not found:
            mini2=0
        mini=mini2
    log(mini, maxi)

    #print max, maxi
    return array[mini:maxi+1]
testArray = [ 2,1,1,-5 ]



# Dictionary of input : expected output test cases
inCases = []
outCases = []
def addTestCase( inp, outp ):
    inCases.append(inp)
    outCases.append(outp)
    assert len(inCases)==len(outCases)

def runAllTestCases(func):
    global __debugMode
    assert len(inCases)==len(outCases)
    for i in range(len(inCases)):
        if not func(inCases[i]) == outCases[i]:
            print "Test %d Failed" % i
            print "input:"
            print inCases[i]
            print "\nExpected output:"
            print outCases[i]
            print "\nCalling %s with tracing" % str(func)
            __debugMode=True
            out = func(inCases[i])
            __debugMode=False
            print "Received output:"
            print out
            exit(-1)
    print "All Tests Passed!\n"



addTestCase( [1,1,1], [1,1,1] )
addTestCase( [1,1,0], [1,1] )
addTestCase( [0,1,1], [1,1] )
addTestCase( [0,1,0], [1] )
addTestCase( [-1,1,0], [1] )
addTestCase( [1,-1,0], [1] )
addTestCase( [1,-1,1], [1] )
addTestCase( [2,-1,1], [2] )
addTestCase( [1,-1,2], [2] )
addTestCase( [2,-1,2], [2,-1,2] )
addTestCase( [2,-2,2], [2] )
addTestCase( [2,-3,2], [2] )
addTestCase( [-3,2], [2] )
addTestCase( [-3,-3], [] )
addTestCase( [-3,0], [] )
addTestCase( [-3,1,0,0,0,1], [1,0,0,0,1] )
addTestCase( [-3,1,0,0,0,1,0,0], [1,0,0,0,1] )
addTestCase( [-3,1,0,0,0,1,-1,0], [1,0,0,0,1] )
addTestCase( [-3,1,0,0,0,1,-1,1], [1,0,0,0,1] )
addTestCase( [-3,1,0,-1,0,1,0,-1,1], [1] )
addTestCase( [-3,1,0,-1,0,1,0,1,-1], [1,0,1] )
addTestCase( [-3,1,0,-1,0,1,-1,1,-1], [1] )
addTestCase( [], [] )
addTestCase( None, [] )
addTestCase( 1, [] )
addTestCase( "foo", [] )
addTestCase( [1,1,-3,1,1], [1,1] )
addTestCase( [1,1,1,-3,1,1,1], [1,1,1] )
addTestCase( [1,0,2,-3,1,0,2], [1,0,2] )
addTestCase( [2,2,-6,1,2,2], [1,2,2] )



runAllTestCases(maxSubarray)

