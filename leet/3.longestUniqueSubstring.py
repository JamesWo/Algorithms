# given a string, return the longest substring that has no duplicate characters.

import sets

def longestUniqueSubstring(s):
    if not s:
        return ""
    lastSeen  = set()
    lastSeen.add(s[0])
    start = 0
    end = 1
    bestStart = 0
    bestEnd = 1
    while end < len(s):
        if s[end] not in lastSeen:
            lastSeen.add(s[end])
            end += 1
        else:
            if ( (end-start) > (bestEnd-bestStart) ):
                bestEnd = end
                bestStart = start
            while True:   
                lastSeen.remove(s[start])
                start += 1
                if s[start-1] == s[end]:
                    break
            lastSeen.add(s[end])
            end += 1
    
    if ( (end-start) > (bestEnd-bestStart) ):
        bestEnd = end
        bestStart = start
    return s[bestStart:bestEnd]

inp = {
"abcdeafg":'bcdeafg',
"abcdeefg":'abcde',
'aaaaa':'a',
'aaaabaaaa':['ab', 'ba'],
'a':'a',
'aa':'a',
'abcdefg':'abcdefg'
}


for test, expected in inp.iteritems():
    if not isinstance(expected, list):
        expected = [expected]
    assert longestUniqueSubstring(test) in expected, "input:%s, got:%s, expected:%s" % (test, longestUniqueSubstring(test), expected)
