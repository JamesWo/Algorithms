# https://www.hackerrank.com/challenges/grid-challenge

def solve(numLines, lines):
    linesMatrix = []
    for line in lines:
        linesMatrix.append(sorted(list(line)))
    for col in range(numLines):
        if not all(linesMatrix[i][col] <= linesMatrix[i+1][col] for i in range(numLines-1)):
            return "NO"
    return "YES"
    
numCases = input()
for _ in range(numCases):
    numLines = input()
    lines = []
    for line in range(numLines):
        lines.append(raw_input())
    print solve(numLines, lines)

