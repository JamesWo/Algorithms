# http://community.topcoder.com/stat?c=problem_statement&pm=13687

class CountryGroup(object):
    def solve(self, arr):
	if not arr:
	    return -1
	index = 1
	totalGroups = 0
	lastSeen = arr[0]
	lastSeenCount = 1
	while index < len(arr):
	    if lastSeen != arr[index]:
		if lastSeenCount != lastSeen:
		    return -1
		lastSeenCount = 1
		lastSeen = arr[index]
		totalGroups += 1
	    elif lastSeen == lastSeenCount:
		lastSeenCount = 1
		totalGroups += 1
	    else:
		lastSeenCount += 1
	    index += 1
	if lastSeenCount != lastSeen:
	    return -1
	return totalGroups + 1
    



s = CountryGroup()

inp = (
[2,2,3,3,3],
[1,1,1,1,1],
[3,3],
[4,4,4,4,1,1,2,2,3,3,3],
[2,1,2,2,1,2],
)

out = (
2,
5,
-1,
5,
-1
)


for i,o in zip(inp, out):
    res = s.solve(i)
    assert res == o, "Failed, input: %s, output: %s, expected: %s" % (i, res, o)
