# Enter your code here. Read input from STDIN. Print output to STDOUT
#k=2 --- 1, 3, -1, -3...
#k=3 --- 0, 2, 4, 6...
#k=4 --- 1234 --- 10, 8, 6, 4, 2, 0...
#k=5 --- 12345 --- 15, 13, 11, 9, ...

def solve(n, k):
    totalSum = sum(range(1, n+1))
    return(totalSum >= abs(k) and totalSum%2 == k%2)

numCases = input()
for _ in range(numCases):
    n, k = map(int, raw_input().split(" "))
    print "YES" if solve(n, k) else "NO"
