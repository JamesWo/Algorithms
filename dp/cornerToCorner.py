import sets
def numWays(rows, cols, xPos):
    """ number of ways robot starting from bottom left can get to top right of grid.
        Robot can only move up or right one space at a time.
        Robot cannot move to any positions in xPos 
    """
    xPosSet = set()
    for elem in xPos:
        xPosSet.add(elem)
    board = [ [0]*cols for _ in range(cols) ]
    board[0][0] = 1
    for row in range(rows):
        for col in range(cols):
            if (row, col) in xPosSet:
                board[row][col] = 0
            elif row == col == 0:
                board[row][col] = 1
            elif row == 0:
                board[row][col] = board[row][col-1]
            elif col == 0:
                board[row][col] = board[row-1][col]
            else:
                board[row][col] = board[row][col-1] + board[row-1][col]
    return board[rows-1][cols-1]


# test

assert numWays(2, 2, []) == 2
assert numWays(2, 2, [(1,0)]) == 1
assert numWays(2, 2, [(0,1)]) == 1
assert numWays(2, 2, [(0,1),(1,0)]) == 0
