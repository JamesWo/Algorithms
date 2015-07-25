#http://community.topcoder.com/stat?c=problem_statement&pm=13668

def flip(c):
    if c == 'A':
        return 'B'
    elif c == 'B':
        return 'A'
    else:
        assert False, 'incorrect flip arg : %s' % c

class TaroFillingAStringDiv2:
    def getNumber(self, s):
        if not s:
            return 0
        l = list(s)
        index = 0
        while index < len(l):
            if l[index] == '?':
                index += 1
            else:
                break
        count = 0 
        while index < len(l):
            if l[index] == '?':
                l[index] = flip(l[index-1])
            if index > 0 and l[index] == l[index-1]:
                count += 1
            index += 1
        return count

tester = TaroFillingAStringDiv2()

cases = {
        "ABAA":1,
        "??":0,
        "A?A":0,
        "A??B???AAB?A???A":3,
        "?BB?BAAB???BAB?B?AAAA?ABBA????A?AAB?BBA?A?":10,
        }

for case, out in cases.iteritems():
    result = tester.getNumber(case)
    if result != out:
        print "Failed test, input = %s" % str(case)
        print "output = %s" % result
        print "expected = %s" % out
        assert False
