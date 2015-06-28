#https://www.hackerrank.com/challenges/pangrams
import sets
import string
inp = raw_input().lower()
chars = set()
for i in range(len(inp)):
    chars.add(inp[i])
    
for char in string.ascii_lowercase:
    if char not in chars:
        print "not pangram"
        break
else:
    print "pangram"
