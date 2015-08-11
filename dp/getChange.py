def count(n):
    """Returns the number of ways to make n cents with quarters, dimes, nickels, and pennies.
    """
    if n >= 25:
        coin = 25
    elif n >= 10:
        coin = 10
    elif n >= 5:
        coin = 5
    else:
        coin = 1
    return countHelper(n, coin)

lowerDenom = { 25:10, 10:5, 5:1, 1:0 }
cache = { 25:{},
          10:{},
          5:{}
          }
global ct
ct = 0
def countHelper(n, coin):
    global ct
    orign = n
    if coin == 0:
        return 0
    if coin == 1:
        return 1
    if n in cache[coin]:
        ct += 1
        return cache[coin][n]
    total = 0
    while n >= 0:
        total += countHelper(n, lowerDenom[coin])
        n -= coin
    cache[coin][orign] = total
    return total

# test

assert count(1) == 1
assert count(4) == 1
assert count(5) == 2
assert count(6) == 2
# n = 10, possible ways
# dimes, nickels, pennies
# 0, 0, 10
# 0, 1, 5
# 0, 2, 0
# 1, 0 0
assert count(10) == 4
assert count(14) == 4
# n = 15, possible ways
# 0 dimes 0 nickel 15 pennies
# 0 dimes 1 nickel 10 pennies
# 0 dimes 2 nickel 5 pennies
# 0 dimes 3 nickel 0 pennies
# 1 dime 0 nickel 5 pennies
# 1 dime 1 nickel 0 pennies
assert count(15) == 6

# some performance tests
import time

numtrials = 3
n = 3000
totaltime = 0
for i in range(numtrials):
    before = time.time()
    print count(n)
    after = time.time()
    totaltime += ( after - before )
print "time taken to run count(%d): %f seconds" % (n, ( totaltime / numtrials ) )
