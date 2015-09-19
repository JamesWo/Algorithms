def solve(s):
    """ returns the longest substring of s that has no repeated characters.
    """
    if not s:
        return ""
    start = 0
    end = 0
    seen = set()
    bestPos = (0,0)
    while end < len(s):
        if s[end] in seen:
            if (end-start) > (bestPos[1]-bestPos[0]):
                bestPos = (start, end)
            while s[start] != s[end]:
                seen.remove(s[start])
                start += 1
            start += 1
        else:
            seen.add(s[end])
        end += 1
    if (end-start) > bestPos[1]-bestPos[0]:
        bestPos = (start, end)
    return s[bestPos[0]:bestPos[1]]

# test

assert solve("abcabcbb") == "abc"
assert solve("b") == "b"



