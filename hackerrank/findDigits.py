#https://www.hackerrank.com/challenges/find-digits
# Enter your code here. Read input from STDIN. Print output to STDOUT
numCases = input()
for _ in range(numCases):
    firstn = input()
    n = firstn
    count = 0
    while n:
        if (n%10) != 0 and firstn%(n%10) == 0:
            count += 1
        n /= 10
    print count
    
