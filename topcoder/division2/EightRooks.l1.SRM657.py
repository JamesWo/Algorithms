# http://community.topcoder.com/stat?c=problem_statement&pm=13773

class EightRooks(object):
    def isCorrect(self, board):
	for row in board:
	    if row.count('R') != 1:
		return "Incorrect"
	for col in range(8):
	    rooksSeen = 0
	    for row in range(8):
		if board[col][row] == 'R':
		    rooksSeen += 1
	    if rooksSeen != 1:
		return "Incorrect"
	return "Correct"


# test

s = EightRooks()

inp = (
["R.......",
 ".R......",
 "..R.....",
 "...R....",
 "....R...",
 ".....R..",
 "......R.",
 ".......R"],

["........",
 "....R...",
 "........",
 ".R......",
 "........",
 "........",
 "..R.....",
 "........"],

["......R.",
 "....R...",
 "...R....",
 ".R......",
 "R.......",
 ".......R",
 "..R.....",
 ".......R"]

)

out = (
"Correct", "Incorrect", "Correct"
)

for k, v in zip(inp, out):
    res = s.isCorrect(k)
    assert res == v, "Failed test, input: %s, expected: %s, actual: %s" % (k, v, res)
