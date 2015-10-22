# Enter your code here. Read input from STDIN. Print output to STDOUT
def isValidBst(lst):
    return validBSTHelper(lst, 0, len(lst), float("-inf"), float("inf"))

def validBSTHelper(lst, start, end, minv, maxv):
    #print start, end, min, max
    if not ( minv < lst[start] < maxv ):
        return False
    if start >= (end-1):
        return True
    root = lst[start]
    index = start + 1
    while index < end and lst[index] <= root:
        if not ( minv < lst[index] < maxv ):
            return False
        index += 1
    #recurse left
    if index > start+1:
        if not validBSTHelper(lst, start+1, index, minv, root):
            return False
    #recurse right
    if index < (end-1):
        if not validBSTHelper(lst, index, end, root, maxv):
            return False
    return True

case = 0
lst = []
while True:
    try:
        inp = raw_input()
    except EOFError:
        break
    if inp:
        inp = map(int, inp.split())
    for i in range(len(inp)):
        if inp[i] >= 0:
            lst.append(inp[i])
        else:
            case += 1
            print "Case " + str(case) + ": " + ("yes" if isValidBst(lst) else "no")
            lst = []
