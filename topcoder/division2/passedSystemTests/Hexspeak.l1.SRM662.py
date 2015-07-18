#http://community.topcoder.com/stat?c=problem_statement&pm=13880

class Hexspeak(object):
    
    def decode(self, num):
	def bitToChar(x):
	    if x == 0:
		return 'O'
	    if x == 1:
		return 'I'
	    if 2 <= x <= 9:
		assert False
	    if x >= 16:
		assert False
	    return hex(x)[2].upper()
	result = []
	while num > 0:
	    lowestBit = num % 16
	    if 2 <= lowestBit <= 9:
		return "Error!"
	    result.append(bitToChar(lowestBit))
	    num /= 16
	result.reverse()
	return "".join(result)

# test

t = Hexspeak()
assert t.decode(16) == 'IO'
assert t.decode(15) == 'F'
assert t.decode(17) == 'II'
assert t.decode(18) == 'Error!'
assert t.decode(257) == 'IOI'
assert t.decode(258) == 'Error!'
assert t.decode(3405691582) == 'CAFEBABE'
assert t.decode(999994830345994239) == 'DEOBIFFFFFFFFFF'
assert t.decode(1000000000000000000) == 'Error!'


