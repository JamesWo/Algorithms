#https://www.hackerrank.com/challenges/taum-and-bday
# Enter your code here. Read input from STDIN. Print output to STDOUT
def minCost(numBlack, numWhite, costBlack, costWhite, costSwap):
    """ Returns the minimum cost to buy numWhite and numBlack
    gifts, given the costs of black, white and swapping.
    """
    trueCostBlack = min(costBlack, costWhite+costSwap)
    trueCostWhite = min(costWhite, costBlack+costSwap)
    return numBlack * trueCostBlack + numWhite * trueCostWhite
    
numCases = input()
for _ in range(numCases):
    numBlack, numWhite = map(int, raw_input().split(" "))
    costBlack, costWhite, costSwap = map(int, raw_input().split(" "))
    print minCost(numBlack, numWhite, costBlack, costWhite, costSwap)
