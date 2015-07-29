#http://community.topcoder.com/stat?c=problem_statement&pm=13719


def flip(char):
    assert char in ('W', 'B')
    return "B" if char == "W" else "W"

class BichromeBoard(object):
    board = None
    def fillRow(self, rowNum, startIndex):
        row = self.board[rowNum]
        for i in range(startIndex+1, len(row)):
            if row[i] == row[i-1]:
                return False
            row[i] = flip(row[i-1])
        for i in range(startIndex-1, -1, -1):
            if row[i] == row[i+1]:
                return False
            row[i] = flip(row[i+1])
        return True

    def fillCol(self, colNum, startIndex):
        for i in range(startIndex+1, len(self.board)):
            if self.board[i][colNum] == self.board[i-1][colNum]:
                return False
            self.board[i][colNum] = flip(self.board[i-1][colNum])
        for i in range(startIndex-1, -1, -1):
            if self.board[i][colNum] == self.board[i+1][colNum]:
                return False
            self.board[i][colNum] = flip(self.board[i+1][colNum])
        return True

    def getFirstColored(self):
        for rowIndex in range(len(self.board)):
            for colIndex in range(len(self.board[rowIndex])):
                if self.board[rowIndex][colIndex] == '?':
                    continue
                else:
                    return (rowIndex, colIndex)
        return False

    def ableToDraw(self, stringArr):
        self.board = []
        for row in stringArr:
            newRow = []
            for char in row:
                newRow.append(char)
            self.board.append(newRow)
        start = self.getFirstColored()
        if not start:
            # the board was all '?'
            return "Possible"
        startRow, startCol = start
        if not self.fillRow(startRow, startCol):
            return "Impossible"
        for colIndex in range(len(self.board[0])):
            if not self.fillCol(colIndex, startRow):
                return "Impossible"
        return "Possible"

# test

cases = {
        
("W?W",
 "??B",
 "???") : "Possible",
        
("W??W",): "Impossible",
        
("??",): "Possible",
        
("W???",
 "??B?",
 "W???",
 "???W"): "Possible",
        
("W???",
 "??B?",
 "W???",
 "?B?W"): "Impossible",
        
("B",): "Possible",

}

tester = BichromeBoard()

for inp, expected in cases.iteritems():
    result = tester.ableToDraw(list(inp))
    if result != expected:
        print "input: ", inp
        print "result: ", result
        print "expected: ", expected
        assert False

