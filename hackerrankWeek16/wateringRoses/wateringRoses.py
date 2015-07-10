""" 
Finds the lowest-cost of placing sprinklers with range width.
Returns a dict with two entries:
    'cost' : cost of the best solution
    'solution' : ( numSprinklers, width, arrayOfPositions )
"""
def getOptimalSolution( width, sprinklerCost, upgradeCost, previousOpenPosition, numRoses ):
    # width is how many roses to the left and to the right each sprinker can water
    # i.e. width == 2 means
    # 0 0 1 1 x 1 1 0 0 0
    # sprinker placed at 'x' can water itself and all the '1'

    # find how many sprinklers we need
    # greedy algorithm: place each sprinkler as far right as possible
    # if that position is occupied, place it to the left as close as possible
    # if we ever try to place a sprinker in a position in which we already
    # 	placed one, then it is impossible to solve the problem with the
    #	given width.
    cost = upgradeCost * width
    placedSprinklers = []
    # note that we are 1-indexed.  Start at the first position that can also water the first rose
    currPos = 1 + width
    while currPos <= numRoses:
	currPos = previousOpenPosition[currPos]
	if currPos == -1:
	    return False
	# place a sprinker at currPos
	if placedSprinklers and placedSprinklers[-1] == currPos:
	    return False
	placedSprinklers.append(currPos)
	currPos += ( 2*width + 1 )
	   
    while placedSprinklers[-1] + width  < numRoses:
	currPos = placedSprinklers[-1] + width + 1
	if currPos > numRoses:
	    break
	currPos = previousOpenPosition[currPos]
	if currPos == placedSprinklers[-1]:
	    return False
	placedSprinklers.append(currPos)
    numSpinklersPlaced = len(placedSprinklers)
    cost += numSpinklersPlaced*sprinklerCost
    return { 'cost' : cost,
	     'solution' : ( numSpinklersPlaced, width, placedSprinklers )
	    }

def solve():
    numRoses, numAllowedPositions, sprinklerCost, upgradeCost = map(int, raw_input().split(" "))
    allowedPositions = map(int, raw_input().split(" "))
    previousOpenPosition = {}
    lastSeen = -1
    allowedPosIndex = 0
    for i in range(1, numRoses+1):
	if allowedPosIndex < numAllowedPositions and i == allowedPositions[allowedPosIndex]:
	    allowedPosIndex += 1
	    lastSeen = i
	previousOpenPosition[i] = lastSeen

    bestCost = float('inf')
    # we need to store the following from the best solution
    # ( numSprinklers, width, arrayOfPositions )
    bestCostSolution = None
    for width in range(numRoses):
	answer = getOptimalSolution(width, sprinklerCost, upgradeCost, previousOpenPosition, numRoses)
	if not answer:
	    continue
	if answer['cost'] < bestCost:
	    bestCost = answer['cost']
	    bestCostSolution = answer['solution']

    print bestCostSolution[0], bestCostSolution[1]
    print " ".join(map(str,bestCostSolution[2]))


numTestCases = input()
for _ in range(numTestCases):
    solve()







