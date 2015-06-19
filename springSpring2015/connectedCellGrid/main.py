# source from 
# https://www.hackerrank.com/contests/springsprint/challenges/connected-cell-in-a-grid
# 2015 hackerrank spring sprint

# Enter your code here. Read input from STDIN. Print output to STDOUT
import pprint
pp = pprint.PrettyPrinter(indent=2)

rows = input()
columns = input()

#while(columns == rows and rows==4):
#    ttt=3+4
#    tttt=ttt**3
#    ttt%235

matrix = []
for r in range(rows):
    row = map(int, raw_input().rsplit())
    matrix.append(row)
#print pp.pprint(matrix)

def handleRegion(i, j, count, depth):
    assert (matrix[i][j]==1), "called handleRegion on non-filled cell"
    matrix[i][j] = 0
    count[0] += 1
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            if (ii == i and jj == j):
                continue
            if (ii < 0 or ii > rows-1):
                continue
            if (jj < 0 or jj > columns-1):
                continue    
            if (matrix[ii][jj] == 1):
                handleRegion(ii, jj, count, depth)
    return count[0]
            
    
#while(1):
#   pass

def findRegion():
    bestSize = 0
    for i in range(rows):
        for j in range(columns):
            
            if matrix[i][j]:
                depth = 0
                regionSize = handleRegion(i, j, [0], [0])
                if regionSize > bestSize:
                    bestSize = regionSize
    return bestSize
    
print findRegion()


