# reverse a string
# benchmark different methods
# to add an implementation, define the function and add the function to funcs

import timeit
import string
import random

def reverse1(string):
    strlen = len(string)
    newstring = ""
    for i in range(strlen-1, -1, -1):
        newstring += string[i]
    return newstring

def reverse2(string):
    return string[::-1]

def reverse3(string):
    return "".join(x for x in reversed(string)) 

def reverse4(string):
    strlen = len(string)
    newstring = ""
    for i in xrange(strlen-1, -1, -1):
        newstring += string[i]
    return newstring

funcs = [reverse1, reverse2, reverse3, reverse4]
# reverse2 is the fastest by about 50x all the others

testCases = {
    "":"",
    "a":"a",
    "ab":"ba",
    "abc":"cba",
    "cba":"abc",
    "aaab":"baaa"
        }

# make sure our functions work
for inp, outp in testCases.iteritems():
    for func in funcs:
        if func(inp) != outp:
            print "Test failed on input: %s; output: %s; expected: %s" % (inp, outp, func(inp))
            exit(-1)

# benchmark the functions

# randomly generate some strings
charSet = string.ascii_uppercase + string.ascii_lowercase + string.digits
low, high = 500, 1000
testStrings = [ "".join(random.choice(charSet) for _ in range(random.randrange(low, high))) for _ in range(10) ]

numRuns = 1000

print "Running benchmarks on randomly generated strings with length in range(%d, %d)" % (low, high)
for func in funcs:
    print "Average time taken to run %s once (in microseconds): %f" % (func, 
            timeit.timeit("for s in testStrings:\n    func(s)",
                          number=numRuns,
                          setup="from __main__ import func, testStrings")*1000000 / ( 
                              len(testStrings)*numRuns ) )


