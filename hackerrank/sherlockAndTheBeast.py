#https://www.hackerrank.com/challenges/sherlock-and-the-beast

# Enter your code here. Read input from STDIN. Print output to STDOUT
def maxDecentNum(numDigits):
    for i in range(numDigits, max(-1, numDigits-(3*5)-1), -1):
        if i % 3 == 0 and (numDigits-i) % 5 == 0:
            return int("5"*i + "3" * (numDigits-i))
    return -1
    
numCases = input()
for _ in range(numCases):
    numDigits = input()
    print maxDecentNum(numDigits)
