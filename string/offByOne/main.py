def isMatch(i1, s1, i2, s2):
    if i1 >= len(s1) and i2 >= len(s2):
        return True
    if i1 >= len(s1) or i2 >= len(s2):
        return False
    return ((s1[i1] == s2[i2]) and isMatch(i1+1, s1, i2+1, s2))

def offByOne(s1, s2):
    index = 0
    while True:
        if index >= len(s1):
            return ((len(s2)-index) <= 1)
        if index >= len(s2):
            return ((len(s1)-index) <= 1)
        if s1[index] == s2[index]:
            index += 1
            continue
        else:
            return ( isMatch(index+1, s1, index, s2) or \
                     isMatch(index, s1, index+1, s2) or \
                     isMatch(index+1, s1, index+1, s2) )


# test isMatch
assert isMatch(0, "abc", 0, "abc")
assert not isMatch(1, "abc", 0, "abc")
assert isMatch(1, "dabc", 0, "abc")
assert not isMatch(1, "abc", 1, "abcd")
assert isMatch(1, "abc", 2, "aabc")

# test offByOne
assert offByOne( 'abcde', 'abcde' )
assert offByOne( 'azcde', 'abcde' )
assert offByOne( 'abzcde', 'abcde' )
assert offByOne( 'abcde', 'abczde' )

assert not offByOne( 'abcdefg', 'abcde' )
assert not offByOne( '', 'ae' )
assert offByOne( 'abcdefg', 'abcdeg' )
assert not offByOne( 'abcdefg', 'abcdez' )
