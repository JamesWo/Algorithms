# Enter your code here. Read input from STDIN. Print output to STDOUT
numCases = input()
for _ in range(numCases):
    n = input()
    print "%d is %s" % (n, ("even" if n%2==0 else "odd"))

