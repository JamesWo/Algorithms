"""
# [AlienAndGame](http://community.topcoder.com/tc?module=ProblemDetail&rd=15838&pm=12821)
*Single Round Match 605 Round 1 - Division II, Level Two*

## Statement
Alien Fred wants to destroy the Earth.
But before he does that, he wants to play the following game.

He has a rectangular board divided into unit cells.
Each cell is initially painted black or white.
You are given a String[] *board*.
The character *board*[i][j] represents the cell with coordinates (i, j).
Each of those characters is either 'B' (representing a black cell) or 'W' (representing a white cell).
The game is played in turns.
In each turn Fred can choose any row of the board and repaint all black cells of the row to white, and vice versa.
(Note that he can only select rows, not columns. 
Formally, he can choose an index i and change all characters of *board*[i].)

Fred wants to have a large white square somewhere on his board.
The sides of Fred's square must be parallel to the sides of the board.
The white square may be a part of a larger white area. 
(I.e., the cells that touch the square may be both black and white.)
Find a sequence of turns that produces the largest possible white square somewhere on the board, and return the area of that square.

## Definitions
- *Class*: `AlienAndGame`
- *Method*: `getNumber`
- *Parameters*: `String[]`
- *Returns*: `int`
- *Method signature*: `int getNumber(String[] board)`

## Constraints
- *board* will contain between 1 and 50 elements, inclusive.
- Each element of *board* will contain between 1 and 50 characters, inclusive.
- Each element of *board* will contain the same number of characters.
- Each character in each element of *board* will be either 'B' or 'W'.

## Examples
### Example 1
#### Input
<c>["BB",<br /> "WW"]</c>
#### Output
<c>4</c>
#### Reason
The optimal strategy is to repaint row 0. After this change the entire board will be white, and thus we have a 2*2 white square.

### Example 2
#### Input
<c>["W"]</c>
#### Output
<c>1</c>
#### Reason
Sometimes the optimal strategy requires no repainting.

### Example 3
#### Input
<c>["WBBB",<br /> "WBBB",<br /> "WWWW"]</c>
#### Output
<c>9</c>
#### Reason
We should repaint row 0 and then repaint row 1. 
The resulting board will contain a 3*3 white square (in rows 0-2 and columns 1-3).

### Example 4
#### Input
<c>["W",<br /> "B",<br /> "W",<br /> "W",<br /> "W"]</c>
#### Output
<c>1</c>
### Example 5
#### Input
<c>["BWBBWBB",<br /> "WWBWWBW",<br /> "BBBBBBW",<br /> "WBBBBWB",<br /> "BBWWWWB",<br /> "WWWWWWW",<br /> "BBWWBBB"]</c>
#### Output
<c>9</c>
"""

def possibleIndex( seq, size, row, col ):
    """ Returns whether or not it is possible
    to create a size*size box with the top-left
    corner at ( row, col ).  """
    for r in range( row, row+size ):
        if seq[r][col] < size:
            return False
    return True

def possibleIndexSlow( board, size, i, j ):
    for row in range(i, i+size):
        first = board[row][j]
        for col in range(j, j+size):
            if board[row][col] != first:
                return False
    return True

def possible( board, seq, size ):
    """ Try every possible starting position
    in the board, and attempt to make a size*size
    box. """
    for i in range( len(board)+1-size ):
        for j in range( len( board[0] )+1-size ):
            #if possibleIndexSlow( board, size, i, j):
            if possibleIndex( seq, size, i, j ):
                return True
    return False

def getNumber(board):
    starts = []
    for i in range(len(board)):
        row = board[i]
        seq = []
        last = row[-1]
        ct = 0
        for j in range(len(row)-1, -1, -1):
            if row[j] == last:
                ct += 1
            else:
                last = row[j]
                ct = 1
            seq.append(ct)
        seq.reverse()
        starts.append( seq )
    for size in range( len(board), -1, -1 ):
        if possible( board, starts, size ):
            return size * size
    assert False, "unreachable"


