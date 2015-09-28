#https://www.hackerrank.com/challenges/chocolate-feast
# Enter your code here. Read input from STDIN. Print output to STDOUT
def calculateCandy(dollars, cost, wrappersForDollar):
    bought = dollars/cost
    wrappers = bought
    while wrappers >= wrappersForDollar:
        more = (wrappers/wrappersForDollar)
        bought += more
        wrappers %= wrappersForDollar
        wrappers += more
    return bought
    return bought

numCases = input()
for _ in range(numCases):
    dollars, cost, wrappersForDollar = map(int, raw_input().split(" "))
    print calculateCandy(dollars, cost, wrappersForDollar)

