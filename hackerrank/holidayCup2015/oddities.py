#https://www.hackerrank.com/contests/round-1-holiday-cup/challenges/oddities

# Enter your code here. Read input from STDIN. Print output to STDOUT
numCases = input()
for _ in range(numCases):
    n = input()
    print "%d is %s" % (n, ("even" if n%2==0 else "odd"))
