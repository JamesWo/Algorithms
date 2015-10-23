# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(grid, rows, cols):
    direction = None
    curr = None
    for c in range(cols):
        if grid[0][c] == "*":
            direction = "down"
            curr = [1, c]
            break
        if grid[rows-1][c] == "*":
            direction = "up"
            curr = [rows-2, c]
            break
    else:
        for r in range(rows):
            if grid[r][0] == "*":
                direction = "right"
                curr = [r, 1]
                break
            if grid[r][cols-1] == "*":
                direction = "left"
                curr = [r, cols-2]
                break
            
    assert direction is not None
    assert curr is not None
    
    while True:
        if curr[0] == 0 or curr[0] == (rows-1) or curr[1] == 0 or curr[1] == (cols-1):
            return curr
        
        if grid[curr[0]][curr[1]] == "/":
            if direction == "left":
                direction = "down"
            elif direction == "right":
                direction = "up"
            elif direction == "down":
                direction = "left"
            elif direction == "up":
                direction = "right"
        
        elif grid[curr[0]][curr[1]] == "\\":
            if direction == "left":
                direction = "up"
            elif direction == "right":
                direction = "down"
            elif direction == "down":
                direction = "right"
            elif direction == "up":
                direction = "left"

        if direction == "left":
            curr[1] -= 1
        elif direction == "right":
            curr[1] += 1
        elif direction == "down":
            curr[0] += 1
        elif direction == "up":
            curr[0] -= 1

case = 1
while True:
    raw_inp = raw_input()
    cols, rows = map(int, raw_inp.split(" "))
    if rows == 0 and cols == 0:
        break
    grid = []
    for _ in range(rows):
        grid.append(list(raw_input().strip()))
    result = solve(grid, rows, cols)
    grid[result[0]][result[1]] = "&"
    print "HOUSE %d" % case
    case += 1
    for row in grid:
        print "".join(row)
