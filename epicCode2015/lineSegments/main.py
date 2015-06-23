#https://www.hackerrank.com/contests/epiccode/challenges/line-segments

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

numLines = input()
lines = []
for i in range(numLines):
    lines.append(map(int, raw_input().split(" ")))
lines = sorted(lines, key=lambda x:x[1], reverse=True)
lines = sorted(lines, key=lambda x:x[0])

#last = lines[0][0]
#for i in range(1,numLines):
#    if lines[i][0] == last:
#        lines[i][1] = 0
#    last = lines[i][0]

lines = map(lambda x:x[1], lines)

S = []
S.append(lines[0])
lenS = 1
for num in lines:
    if num > S[-1]:
        S.append(num)
        lenS += 1
        continue
    # find the smallest number in S that is >= num
    # use binary search
    lo = 0
    hi = lenS-1
    while lo <= hi: 
        mid = int(math.ceil((lo+hi)/2.0))
        if S[mid] < num:
            lo = mid+1
        else:
            hi = mid-1
    S[lo] = num

print len(S)


