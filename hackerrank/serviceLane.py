#https://www.hackerrank.com/challenges/service-lane
# Enter your code here. Read input from STDIN. Print output to STDOUT

freewayLength, numCases = map(int, raw_input().split(" "))
widths = map(int, raw_input().split(" "))
for _ in range(numCases):
    start, end = map(int, raw_input().split(" "))
    print min(widths[start:end+1])
