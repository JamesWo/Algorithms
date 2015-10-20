#https://www.hackerrank.com/challenges/sherlock-and-squares
# Enter your code here. Read input from STDIN. Print output to STDOUT
def numSquares(x, y):
    i = 1
    count = 0
    while i**2 <= y:
        if i**2 >= x:
            count += 1
        i += 1
    return count

numCases = input()
for _ in range(numCases):
    x, y = map(int, raw_input().split(" "))
    print numSquares(x, y)
