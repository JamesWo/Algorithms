# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = raw_input()
k = input()
for i in range(0,len(inp),k):
    s = inp[i:i+k]
    news = []
    seen = set()
    for char in s:
        if char not in seen:
            news.append(char)
            seen.add(char)
    print "".join( news )
