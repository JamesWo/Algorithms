#https://www.hackerrank.com/challenges/game-of-thrones
def solve(s):
    if not s or not isinstance(s, str):
        return False
    chars = {}
    for char in s:
        chars[char] = 1 if char not in chars else ( chars[char]+1 )
    odds = 0
    for val in chars.itervalues():
        if val % 2 != 0:
            odds += 1
    return odds <= 1

s = raw_input()
print "YES" if solve(s) else "NO"
