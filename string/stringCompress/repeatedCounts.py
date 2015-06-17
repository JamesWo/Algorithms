# string compression
# assumes original string contains no numbers

def compress1(string):
    # basic method using new string
    newString = ""
    lastChar = None
    lastCount = 0
    for currentChar in string:
        if currentChar != lastChar:
            if lastCount == 1:
                newString += lastChar
            elif lastCount > 1:
                newString += "%c%d" % (lastChar, lastCount)
            lastChar = currentChar
            lastCount = 1
        else:
            lastCount += 1
    newString += "%c" % lastChar
    if lastCount > 1:
        newString += "%d" % lastCount
    return newString

def expand1(string):
    #basic expansion using new string
    newString = ""
    lastChar = None
    for char in string:
        if char.isalpha():
            lastChar = char
            newString += char
        else:
            repeat = int(char)
            newString += lastChar*(repeat-1)
    return newString

def compress2(string):
    # in-place compress
    # does not work since python strings are immutable, and making
    # a list within this function defeats the purpose...
    pass

testStrings = [
        ("abc", "abc"),
        ("abbc", "ab2c"),
        ("abbbc", "ab3c"),
        ("aabbcc", "a2b2c2"),
        ("aabbbbbc", "a2b5c"),
        ]

for orig, expected in testStrings:
    compressed = compress1(orig)
    assert compressed == expected
    assert expand1(compressed) == orig
