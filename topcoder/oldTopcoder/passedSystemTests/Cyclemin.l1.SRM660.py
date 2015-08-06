# cyclemin
# http://community.topcoder.com/stat?c=problem_statement&pm=13814
def rotate(string, num):
    return list(string[num:]+string[:num])

class Cyclemin(object):
    # @param string, integer
    # @return string
    def bestmod( self, s, maxChange ):
	best = s
	for i in range(len(s)):
	    rotated = rotate(s, i)
	    j=0
	    changed=0
	    while changed < maxChange:
		if j >= len(s):
		    return "".join(rotated)
		if rotated[j] == 'a':
		    j += 1
		else:
		    rotated[j] = 'a'
		    j += 1
		    changed += 1
	    rotated = "".join(rotated)
	    best = min(best, rotated)
	return best

s = Cyclemin()

assert s.bestmod('isgbiao', 2) == 'aaaisgb', s.bestmod('isgbiao', 2)
assert s.bestmod('abacaba', 1) == 'aaaabac', s.bestmod('abacaba', 1)
