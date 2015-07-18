class FilipTheFrog(object):
    def countReachable(self, islands, jump):
        # islands is originally a tuple
        islands = list(islands)
	start = islands[0]
	islands.sort()
	index = 0
	while islands[index] != start:
	    index += 1
	pos = index
	total = 1
	while pos < len(islands)-1 and ((islands[pos] + jump) >= islands[pos+1]):
	    pos += 1
	    total += 1
	pos = index
	while pos > 0 and ((islands[pos] - jump) <= islands[pos-1]):
	    pos -= 1
	    total += 1
	return total


inputs = {
( (4, 7, 1, 3, 5), 1 ) : 3,
( (100, 101, 103, 105, 107), 2 ) : 5,
( (17, 10, 22, 14, 6, 1, 2, 3), 4 ) : 7, 
( (0,), 1000 ) : 1,
}


s = FilipTheFrog()
for k,v in inputs.iteritems():
    result = s.countReachable( list(k[0]), k[1] ) 
    assert result == v, "input: %s, %s, \nexpected output: %s\nactual output: %s" % (k[0], k[1], v, result )
