"""
# [FoxAndGo](http://community.topcoder.com/tc?module=ProblemDetail&rd=15702&pm=12743)
*Single Round Match 590 Round 1 - Division II, Level Two*

## Statement
Fox Ciel is teaching her friend Jiro to play Go.
Ciel has just placed some white and some black tokens onto a board.
She now wants Jiro to find the best possible move.
(This is defined more precisely below.)

You are given a String[] *board*.
Character j of element i of *board* represents the cell (i,j) of the board:
'o' is a cell with a white token, 'x' a cell with a black token, and '.' is an empty cell.
At least one cell on the board will be empty.

Jiro's move will consist of adding a single black token to the board.
The token must be placed onto an empty cell.
Once Jiro places the token, some white tokens will be removed from the board according to the rules described in the next paragraphs.

The white tokens on the board can be divided into connected components using the following rules:
If two white tokens lie in cells that share an edge, they belong to the same component.
Being in the same component is transitive: if X lies in the same component as Y and Y lies in the same component as Z, then X lies in the same component as Z.

Each component of white tokens is processed separately.
For each component of white tokens we check whether it is adjacent to an empty cell.
(That is, whether there are two cells that share an edge such that one of them is empty and the other contains a white token from the component we are processing.)
If there is such an empty cell, the component is safe and its tokens remain on the board.
If there is no such empty cell, the component is killed and all its tokens are removed from the board.

Jiro's score is the total number of white tokens removed from the board after he makes his move.
Return the maximal score he can get for the given board.

## Definitions
- *Class*: `FoxAndGo`
- *Method*: `maxKill`
- *Parameters*: `String[]`
- *Returns*: `int`
- *Method signature*: `int maxKill(String[] board)`

## Notes
- The position described by *board* does not have to be a valid Go position. In particular, there can already be components of white tokens that have no adjacent empty cell.
- Please ignore official Go rules. The rules described in the problem statement are slightly different. For example, in this problem the black tokens cannot be killed, and it is allowed to place the black token into any empty cell.

## Constraints
- n will be between 2 and 19, inclusive.
- *board* will contain exactly n elements.
- Each element in *board* will contain exactly n characters.
- Each character in *board* will be 'o', 'x' or '.'.
- There will be at least one '.' in *board*.

## Examples
### Example 1
#### Input
<c>[".....",<br /> "..x..",<br /> ".xox.",<br /> ".....",<br /> "....."]</c>
#### Output
<c>1</c>
#### Reason
To kill the only white token, Jiro must place his black token into the cell (3,2). (Both indices are 0-based.)

### Example 2
#### Input
<c>["ooooo",<br /> "xxxxo",<br /> "xxxx.",<br /> "xxxx.",<br /> "ooooo"]</c>
#### Output
<c>6</c>
#### Reason
By placing the token to the cell (2,4) Jiro kills 6 white tokens. The other possible move only kills 5 tokens.

### Example 3
#### Input
<c>[".xoxo",<br /> "ooxox",<br /> "oooxx",<br /> "xoxox",<br /> "oxoox"]</c>
#### Output
<c>13</c>
#### Reason
There is only one possible move. After Jiro makes it, all the white tokens are killed.

### Example 4
#### Input
<c>[".......",<br /> ".......",<br /> ".......",<br /> "xxxx...",<br /> "ooox...",<br /> "ooox...",<br /> "ooox..."]</c>
#### Output
<c>9</c>
#### Reason
Regardless of where Jiro moves, the 9 white tokens in the lower left corner will be killed.

### Example 5
#### Input
<c>[".......",<br /> ".xxxxx.",<br /> ".xooox.",<br /> ".xo.ox.",<br /> ".xooox.",<br /> ".xxxxx.",<br /> "......."]</c>
#### Output
<c>8</c>
### Example 6
#### Input
<c>["o.xox.o",<br /> "..xox..",<br /> "xxxoxxx",<br /> "ooo.ooo",<br /> "xxxoxxx",<br /> "..xox..",<br /> "o.xox.o"]</c>
#### Output
<c>12</c>
### Example 7
#### Input
<c>[".......",<br /> "..xx...",<br /> ".xooox.",<br /> ".oxxox.",<br /> ".oxxxo.",<br /> "...oo..",<br /> "......."]</c>
#### Output
<c>4</c>
### Example 8
#### Input
<c>[".ox....",<br /> "xxox...",<br /> "..xoox.",<br /> "..xoox.",<br /> "...xx..",<br /> ".......",<br /> "......."]</c>
#### Output
<c>5</c>
### Example 9
#### Input
<c>["...................",<br /> "...................",<br /> "...o..........o....",<br /> "................x..",<br /> "...............x...",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "...................",<br /> "................o..",<br /> "..x................",<br /> "...............x...",<br /> "...................",<br /> "..................."]</c>
#### Output
<c>0</c>

"""
def bfs( board, row, col, size, empty ):
    # if there is a single place to put a piece to kill the most
    # white pieces, return size, (row, col)
    if row < 0 or row >= len(board) or col < 0 or col >= len(board):
        return
    elif board[row][col] == ".":
        empty.append( ( row, col ) )
    elif board[row][col] in ( "x", "v" ):
        return
    elif board[row][col] == "o":
        size[0] += 1
        board[row][col] = "v" # visited
        for r in ( row-1, row+1 ):
                bfs( board, r, col, size, empty )
        for c in ( col-1, col+1 ):
            bfs( board, row, c, size, empty )
    else:
        assert False

def maxKill(board):
    b = []
    n = len(board)
    for row in board:
        new = []
        for char in row:
            new.append( char )
        b.append( new )
    # maps tuple representing a position to place a piece
    # to the number of black pieces removed from the move.
    positionToSizeMapping = {}
    total = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == "o":
                size = [0]
                empty = []
                bfs( b, row, col, size, empty )
                empty = list( set( empty ) )
                if len(empty) == 0:
                    total += size[0]
                elif len(empty) == 1:
                    if empty[0] in positionToSizeMapping:
                        positionToSizeMapping[ empty[0] ] += size[0]
                    else:
                        positionToSizeMapping[ empty[0] ] = size[0]
    if not positionToSizeMapping:
        return total
    return max( positionToSizeMapping.values() ) + total


