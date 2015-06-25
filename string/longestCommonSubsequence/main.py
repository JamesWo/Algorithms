#
# longest common subsequence between two strings
# dynamic programming solution

def lcs(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    table = [ [0 for _ in xrange(len2)] for __ in xrange(len1) ]
    for i in range(1, len1):
	for j in range(1, len2):
	    if str1[i] == str2[j]:
		table[i][j] = table[i-1][j-1] + 1
	    else:
		table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[len1-1][len2-1]

str1 = raw_input()
str2 = raw_input()
print lcs(str1, str2)
	
