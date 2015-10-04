#https://www.hackerrank.com/challenges/manasa-and-stones
# Enter your code here. Read input from STDIN. Print output to STDOUT
def possibleValues(numStones, a, b):
    possible = set([0])
    for i in range(numStones-1):
        newPossible = set()
        for elem in list(possible):
            newPossible.add(elem+a)
            newPossible.add(elem+b)
        possible = newPossible
    return sorted(list(possible))

numCases = input()
for _ in range(numCases):
    numStones = input()
    a = input()
    b = input()
    print " ".join(map(str, possibleValues(numStones, a, b)))
    
    
    
    
