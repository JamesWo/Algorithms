import string

def count1(S1, S2):
    # create the final string
    s = "".join( S1 ) + "".join( S2 )
    assert all( [ char in string.ascii_lowercase for char in s ] )
    count = len( s )
    isPalindrome = [ [0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)):
        isPalindrome[i][i+1] = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            isPalindrome[i][i+2] = 1
            count += 1
    for seqLen in range(3, len(s)+1):
        for startIndex in range(0, len(s)-seqLen+1 ):
            # check if s[startIndex : startIndex + seqLen] is
            # a palindrome
            # the middle must be a palindrome
            if isPalindrome[startIndex+1][startIndex+seqLen-1] == 0:
                continue
            if s[startIndex] == s[startIndex + seqLen - 1]:
                isPalindrome[startIndex][startIndex+seqLen] = 1
                count += 1
    return count

def count2(S1, S2):
    s = "".join( S1 ) + "".join( S2 )
    assert all( [ char in string.ascii_lowercase for char in s ] )
    count = len( s )
    palindromes = set()
    for i in range(len(s)):
        palindromes.add((i, i+1))
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            palindromes.add((i, i+2))
            count += 1
    while palindromes:
        prev = palindromes.pop()
        if prev[0] == 0 or prev[1] == len(s):
            continue
        if s[prev[0]-1] == s[prev[1]]:
            palindromes.add( (prev[0]-1, prev[1]+1) )
            count += 1
    return count

def count(S1, S2):
    return count2(S1, S2)

