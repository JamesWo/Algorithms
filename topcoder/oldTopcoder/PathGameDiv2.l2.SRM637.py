"""
 Problem Statement for PathGameDiv2
        
Cat Snuke is playing the Path Game.

The Path Game is played on a rectangular grid of square cells. The grid has 2 rows and some positive number of columns. Each cell is either black or white.

A left-to-right path in the grid is a sequence of white cells such that the first cell in the sequence is in the leftmost column, the last cell in the sequence is in the rightmost column, and each pair of consecutive cells shares a common side.

The initial coloring of the grid is such that there is at least one left-to-right path. You are given this initial coloring as a String[] board with two elements. For each i and j, board[i][j] is either '#' (representing a black cell) or '.' (representing a white cell).

Snuke may color some of the white cells black. After he does so, there must still be at least one left-to-right path left on the board. The goal of the game is to color as many cells black as possible. Compute and return the largest number of cells Snuke can color black. (Note that the cells that are already black do not count.)
 
Definition
        
Class:  PathGameDiv2
Method: calc
Parameters:     String[]
Returns:        int
Method signature:       int calc(String[] board)
(be sure your method is public)
    
 
Constraints
-       board will contain 2 elements.
-       Each element in board will contain between 1 and 50 characters, inclusive.
-       All elements in board will have the same length.
-       Each character in board will be '#' or '.'.
-       The grid described by board will contain a left-to-right path.
 
Examples
0)      
        
{"#...."
,"...#."}
Returns: 2
Snuke can color at most two white cells black. One possible final state of the board looks as follows:
#....
..###
1)      
        
{"#"
,"."}
Returns: 0
Snuke can't color any cells.
2)      
        
{"."
,"."}
Returns: 1
3)      
        
{"....#.##.....#..........."
,"..#......#.......#..#...."}
Returns: 13

"""

class PathGameDiv2:
    def calc(self, board):
        topWhite = board[0].find("#")
        botWhite = board[1].find("#")
        if topWhite == -1:
            start = 1
        elif botWhite == -1:
            start = 0
        else:
            start = 1 if botWhite > topWhite else 0
        count = 0
        for index in range(len(board[0])-1):
            if board[start][index+1] == '#':
                start = start ^ 1
            elif board[start^1][index] == '.':
                count += 1
        if board[0][-1] == board[1][-1] == '.':
            count += 1
        return count








cases = {
        
("#...."
,"...#."): 2,
        
("#"
,"."): 0,
        
("."
,"."): 1,
        
("....#.##.....#..........."
,"..#......#.......#..#...."): 13,


}

tester = PathGameDiv2()

for inp, expected in cases.iteritems():
    inp = list(inp)
    result = tester.calc( inp )
    if result != expected:
        print "inp ", inp
        print "result ", result
        print "expected ", expected
        assert False

