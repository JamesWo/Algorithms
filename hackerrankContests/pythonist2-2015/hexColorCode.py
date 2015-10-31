# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
from string import hexdigits
import sys
def findHex( line ):
    i = 0
    while i < len(line):
        if line[i] != "#":
            i += 1
            continue
        # check next 6 letters
        #print line[i:i+7]
        #print [ line[j] in hexdigits for j in range(i+1, i+7 ) ]
        #sys.exit(0)
        if all( ( j < len(line) and line[j] in hexdigits ) for j in range(i+1, i+7) ):
            print line[i:i+7]
            i += 7
        # check next 3 letters
        elif all( ( j < len(line) and line[j] in hexdigits ) for j in range(i+1, i+4) ):
            print line[i:i+4]
            i += 4
        i += 1
        
inblock = False
for i in range(n):
    line = raw_input()
    if "{" in line:
        assert not inblock
        inblock = True
    elif "}" in line:
        assert inblock
        inblock = False
    elif inblock:
        #print line
        findHex( line )
