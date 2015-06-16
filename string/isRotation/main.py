
def isRotation(string1, string2):
    if len(string1) != len(string2):
        return False
    double = string1+string1
    return string2 in double

testCasesTrue = {
    "abcdefg" : "abcdefg",
    "abcdefg" : "bcdefga",
    "abcdefg" : "cdefgab",
    "abcdefg" : "defgabc",
    "abcdefg" : "efgabcd",
    "abcdefg" : "fgabcde",
    "" : "",
    "a" : "a",
        }

testCasesFalse = {
    "" : "a",
    "abc" : "cab",
    "abc" : "ab",
    "aab" : "bab",
    "aab" : "bba",
    "aaabc" : "cbaaa"
    }

for k, v in testCasesTrue.iteritems():
    if not isRotation(k, v):
        print "test 1 failed"
        print "isRotation(%s, %s) = %s" % (str(k), str(v), str(isRotation(k,v)))
        exit(-1)

for k, v in testCasesFalse.iteritems():
    if isRotation(k, v):
        print "test 2 failed"
        print "isRotation(%s, %s) = %s" % (str(k), str(v), str(isRotation(k,v)))
        exit(-1)

print "All tests passed"
