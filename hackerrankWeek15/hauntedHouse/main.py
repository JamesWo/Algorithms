# Hackerrank week15 2015
# haunted house

def solve(arr, n):
    # returns the maximum number of intervals that can be satisfied at once
    startPoints = { x:0 for x in range(n) }
    endPoints = { x:0 for x in range(n) }
    
    count = 0
    # count the number of intervals that are satisfied with n=0
    for start, end in arr:
	startPoints[start]+=1
	endPoints[end]+=1
	if start <= 0:
	    count += 1

    best = count
    lastSatisfied = count
    for num in range(1, n):
	# the number of intervals satisfied with k people is the
	# number of intervals satisfied with k-1 people 
	# plus the number of intervals starting on k
	# minus the number of intervals that ended on k-1
	satisfied = lastSatisfied + startPoints[num] - endPoints[n-1]
	lastSatisfied = satisfied
	best = max(best, satisfied)

    return best


