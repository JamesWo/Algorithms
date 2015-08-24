# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
d={}
for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
ans = sorted( sorted( d.iteritems(), key=lambda x:x[0] ), key=lambda x:x[1], reverse=True)
for i in range(3):
    print ans[i][0], ans[i][1]
