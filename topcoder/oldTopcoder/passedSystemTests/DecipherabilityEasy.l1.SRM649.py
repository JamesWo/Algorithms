#http://community.topcoder.com/stat?c=problem_statement&pm=13658

class DecipherabilityEasy(object):
    def check(self, s, t):
        if len(s) != len(t)+1:
            return "Impossible"
        sindex = 0
        tindex = 0
        foundMismatch= False
        while tindex < len(t):
            if s[sindex] == t[tindex]:
                sindex += 1
                tindex += 1
                continue
            elif foundMismatch:
                return "Impossible"
            else:
                foundMismatch = True
                sindex += 1
        return "Possible"
            



# test

tester = DecipherabilityEasy()

cases = {
("sunuke",
"snuke"):
"Possible",
        
("snuke",
"skue"):
"Impossible",
        
("snuke",
"snuke"):
"Impossible",
        
("snukent",
"snuke"):
"Impossible",
        
("aaaaa",
"aaaa"):
"Possible",
        
("aaaaa",
"aaa"):
"Impossible",
      
        
("topcoder",
"tpcoder"):
"Possible",      
        
("singleroundmatch",
"singeroundmatc"):
"Impossible",
}


for inp, out in cases.iteritems():
    result = tester.check( *inp )
    if result != out:
        print "Failed:"
        print "  input: %s" % str(inp)
        print "  output: %s" % result
        print "  expected: %s" % out
        assert False
