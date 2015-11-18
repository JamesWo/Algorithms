# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input()
vowels = set(["A","E","I","O","U"])
totalA = 0
totalB = 0
for i in range(len(s)):
    count = len(s)-i
    if s[i] in vowels:
        totalB += count
    else:
        totalA += count
if totalA == totalB:
    print "Draw"
elif totalA > totalB:
    print "Stuart", totalA
elif totalA < totalB:
    print "Kevin", totalB








