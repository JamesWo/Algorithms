#https://www.hackerrank.com/contests/hackerrank-hiringsprint/challenges/hr4

# Enter your code here. Read input from STDIN. Print output to STDOUT
import bisect
n = input()
salaries = []
for i in range(n):
    salaries.append(input())
salaries.sort()

numQ = input()
for _ in range(numQ):
    i = bisect.bisect_left(salaries, input())
    print i
    
