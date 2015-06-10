# source from
# https://www.hackerrank.com/contests/springsprint/challenges/identify-smith-numbers
# hackerrank 2015 spring sprint

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input an integer > 0,
# Output an integer, the sum of each digit of x
def sumDigits(x):
    return sum(map(int, str(x)))
    
# Input an integer > 0,
# Output an array with all prime factors of x
def primeFactorization(x):
    ret = []
    i = 2
    while i**2 <= x:
        if x%i == 0:
            x = x/i
            ret.append(i)
        else:
            i += 1
    if x>1:
        ret.append(x)
    return ret
        

x = input()
digits = sumDigits(x)
factors = primeFactorization(x)
sumFactors = sum(map(sumDigits, factors))

if (digits == sumFactors):
    print 1
else:
    print 0

