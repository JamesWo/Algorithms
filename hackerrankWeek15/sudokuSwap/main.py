#Sudoku Swap
#Taken from https://www.hackerrank.com/contests/w15/challenges/sudoku-swap

# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkAllRows(grid):
    """
    Returns a dictionary mapping row number to a pair of indices (x, x) where x appears twice in that row.
    """
    swaps = {}
    for i in range(9):
        tuple = checkRow(grid[i])
        if tuple:
            swaps[i] = tuple
    return swaps

def checkRow(row):
    # Allocate an extra int at index 0, not to be used, but to prevent having to subtract 1 from each value
    counts = {}
    for index, x in enumerate(row):
        if x not in counts:
            counts[x] = index
        else:
            return (counts[x], index)
    return ()        
    
def checkAllCols(grid):
    swaps = {}
    for col in range(9):
        counts = {}
        for row in range(9):
            val = grid[row][col]
            if val not in counts:
                counts[val] = row
            else:
                swaps[col] = (counts[val], row)
                break;
    return swaps

def isValid3x3(grid, x1, y1, x2, y2):
    """ 
    Checks all 3x3 grids are valid if we were to swap (x1,y1) with (x2,y2).
    """
    v1 = grid[x1][y1]
    v2 = grid[x2][y2]
    grid[x1][y1] = v2
    grid[x2][y2] = v1
    for i in range(0,9,3):
        for j in range(0,9,3):
            counts = {}
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    val = grid[ii][jj]
                    if val not in counts:
                        counts[val] = 1
                    else:
                        # restore the state of grid
                        grid[x1][y1] = v1
                        grid[x2][y2] = v2
                        return False
    grid[x1][y1] = v1
    grid[x2][y2] = v2
    return True

def printSolution(x1, y1, x2, y2):
    if x1>x2 or (x1==x2 and y1>=y2):
        return printSolution(x2, y2, x1, y1)
    print "(%d,%d) <-> (%d,%d)" % (x1+1, y1+1, x2+1, y2+1)

def printSolutionFromTuple(tuple1, tuple2):
    return printSolution(tuple1[0], tuple1[1], tuple2[0], tuple2[1])
    
def solve(grid):
    rowSwaps = checkAllRows(grid)
    colSwaps = checkAllCols(grid)
    if not rowSwaps and not colSwaps:
        print "Serendipity"
        return
    if not rowSwaps:
        # the swap was two elements in one row
        columns = colSwaps.keys()
        col1 = columns[0]
        col2 = columns[1]  
        
        # there are two ways to swap back- one per row.  Check both for validity with respect to the 3x3 grid rule.
        if colSwaps[col1] == colSwaps[col2]:
            # there could be two possible ways to fix the sudoku.  Either the original swap, or the swap in the other col.
            numPrintedSolutions = 0
            rowPair = colSwaps[col1]
            if isValid3x3(grid, rowPair[0], col1, rowPair[0], col2):
                printSolution(rowPair[0], col1, rowPair[0], col2)
                numPrintedSolutions += 1
            if isValid3x3(grid, rowPair[1], col1, rowPair[1], col2):
                printSolution(rowPair[1], col1, rowPair[1], col2)
                numPrintedSolutions += 1
            assert numPrintedSolutions > 0
            return
   
        # find which columns the swap was in
        if colSwaps[col1][0] in colSwaps[col2]:
            rowSwapped = colSwaps[col1][0]
        else:
            rowSwapped = colSwaps[col1][1]
            assert rowSwapped in colSwaps[col2]
        printSolution(rowSwapped, col1, rowSwapped, col2)
        
    elif not colSwaps:
        # the swap was two elements in one column
        rows = rowSwaps.keys()
        row1 = rows[0]
        row2 = rows[1]
        # there are two ways to swap back- one per column.  Check both for validity with respect to the 3x3 grid rule.
        
        if rowSwaps[row1] == rowSwaps[row2]:
            # there could be two possible ways to fix the sudoku.  Either the original swap, or the swap in the other row.
            numPrintedSolutions = 0
            colPair = rowSwaps[row1]
            if isValid3x3(grid, row1, colPair[0], row2, colPair[0]):
                printSolution(row1, colPair[0], row2, colPair[0])
                numPrintedSolutions += 1
            if isValid3x3(grid, row1, colPair[1], row2, colPair[1]):
                printSolution(row1, colPair[1], row2, colPair[1])
                numPrintedSolutions += 1
            assert numPrintedSolutions > 0
            return
 
        # find which rows the swap was in
        if rowSwaps[row1][0] in rowSwaps[row2]:
            colSwapped = rowSwaps[row1][0]
        else:
            colSwapped = rowSwaps[row1][1]
            assert colSwapped in rowSwaps[row2]
        printSolution(row1, colSwapped, row2, colSwapped)

    else:
        # Only one swap is possible.  Find the intersection of the row and columns.
        matches = {}
        foundMatches = []
        numPrintedSolutions = 0
        for row, colPair in rowSwaps.iteritems():
            for col in colPair:
                coordinate = (row, col)
                if coordinate not in matches:
                    matches[coordinate] = 1
                else:
                    matches[coordinate] += 1
                    foundMatches.append(coordinate)
                    if len(foundMatches) == 2:
                        printSolutionFromTuple(foundMatches[0], foundMatches[1])
                        numPrintedSolutions += 1

        for col, rowPair in colSwaps.iteritems():
            for row in rowPair:
                coordinate = (row, col)
                if coordinate not in matches:
                    matches[coordinate] = 1
                else:
                    matches[coordinate] += 1
                    foundMatches.append(coordinate)
                    if len(foundMatches) == 2:
                        printSolutionFromTuple(foundMatches[0], foundMatches[1])
                        numPrintedSolutions += 1
        assert numPrintedSolutions == 1, "expected numPrintedSolutions == 1.  actual: %d" % numPrintedSolutions
        return
       
numCases = input()
for caseNumber in range(1, numCases+1):
    grid = []
    for i in range(9):
        grid.append(map(int, raw_input().split(" ")))
    print "Case #%d:" % caseNumber
    solve(grid)

    
# Some test cases        
"""
1
1 2 3 4 1 6 7 8 9
4 5 6 7 8 9 1 2 3
7 8 9 1 2 3 4 5 6
5 3 4 6 5 8 9 7 2
6 1 2 3 9 7 5 4 8
9 7 8 2 4 5 6 3 1
3 4 7 9 6 2 8 1 5
2 9 5 8 7 1 3 6 4
8 6 1 5 3 4 2 9 7

Case #1:
(1,5) <-> (4,5)
"""

"""
2
2 1 9 7 5 3 4 8 6
3 7 5 8 6 4 9 1 2
8 4 6 2 9 1 3 5 7
1 9 8 6 7 5 2 4 3
5 6 4 1 3 2 7 9 8
7 2 3 4 8 9 5 6 1
4 4 7 3 1 6 8 2 9
9 8 1 5 2 7 6 3 4
6 3 2 9 5 8 1 7 5
4 6 2 5 7 1 9 8 3
7 9 1 2 8 3 4 6 5
5 8 3 6 4 9 2 7 1
6 1 7 4 9 8 5 3 2
9 4 8 3 5 2 6 1 7
2 3 5 1 6 7 8 9 4
1 7 6 9 2 4 3 5 8
3 5 4 8 1 6 7 2 9
8 2 9 7 3 5 1 4 6

Case #1:
(7,2) <-> (9,5)
Case #2:
Serendipity
"""

"""
1
2 1 9 7 5 3 4 8 6
3 5 7 8 6 4 9 1 2
8 4 6 2 9 1 3 5 7
1 9 8 6 7 5 2 4 3
5 6 4 1 3 2 7 9 8
7 2 3 4 8 9 5 6 1
4 5 7 3 1 6 8 2 9
9 8 1 5 2 7 6 3 4
6 3 2 9 4 8 1 7 5
Case #1:
(2,2) <-> (2,3)
(7,2) <-> (7,3)
"""

"""
1
3 6 7 1 5 2 8 9 4
8 9 1 3 6 4 2 7 5
5 2 4 8 7 9 3 6 1
7 5 9 3 8 6 1 4 2
2 4 8 7 3 1 6 5 9
6 1 3 4 9 5 7 2 8
1 7 2 9 4 3 5 8 6
4 8 5 6 1 7 9 3 2
9 3 6 5 2 8 4 1 7

Case #1:
(4,4) <-> (4,9)
"""

