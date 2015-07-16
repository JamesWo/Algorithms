#http://community.topcoder.com/stat?c=problem_statement&pm=13783

def gcd(x, y):
    # This can be done using fractions.gcd, but wheres the fun in doing that?
    while y:
	tmp = y
	y = x % y
	x = tmp
    return x

def testGcd(numTimesToTest):
    import fractions
    import random
    for i in range(numTimesToTest):
	x = random.randint(-10000,100000)
	y = random.randint(-10000,100000)
	assert gcd(x, y) == fractions.gcd(x, y)
	print "gcd of %d and %d is %d" % (x, y, gcd(x,y))

#testGcd(100000)

class InfiniteString(object):
    def equal(self, s1, s2):
	gcdRes = gcd(len(s1), len(s2))
	return "Equal" if ( s1*(len(s2)/gcdRes) == s2*(len(s1)/gcdRes) ) else "Not Equal"

# test

s = InfiniteString()

inp = {
('ab', 'abab') : 'Equal',
('ababab', 'abab') : 'Equal',
('a', 'z') : 'Not Equal',
('abab', 'aba') : 'Not Equal',
('abc', 'bca') : 'Not Equal'
}

for k, v in inp.iteritems():
    result = s.equal( k[0], k[1] )
    assert result == v, "failed with input %s, output %s, expected %s" % ( str(k), str(v), str(result) )

