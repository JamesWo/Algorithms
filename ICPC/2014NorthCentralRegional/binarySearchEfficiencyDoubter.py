# Enter your code here. Read input from STDIN. Print output to STDOUT
def solve(n):
    total = 0
    exp = 1
    totalct = 0
    while totalct + 2**(exp-1) <=n :
        totalct += 2**(exp-1)
        total += (2**(exp-1))*exp
        exp += 1
    total += (n-totalct)*exp
    return total

case = 0
while True:
    try:
        n = raw_input()
    except EOFError:
        break
    lst = n.split()
    nums = map(int, lst)
    for n in nums:
        case += 1
        print "Case %d: %d" % (case, solve(n))
