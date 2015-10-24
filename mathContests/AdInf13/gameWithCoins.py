# Enter your code here. Read input from STDIN. Print output to STDOUT
numCases = input()
for _ in range(numCases):
    left, right = map(int, raw_input().split(" "))
    if left==0 or right==0 or (left+right)%2==1:
        print "First"
    else:
        print "Second"
