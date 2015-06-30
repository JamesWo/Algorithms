def next(s):
    if not s:
        return False
    for i in range(len(s)-2, -1, -1):
        print i
        if ord(s[i]) < ord(s[i+1]):
            s = swap(s, i)
            print s
            s = s[:i+1] + s[i+1:][::-1]
            print i
            return s

def swap(s, i):
    # linear scan solution
    start = s[i]
    for index in range(i+1, len(s)):
        if index == len(s)-1 or ord(s[index+1]) <= ord(start):
            break
    return s[:i] + s[index] + s[i+1:index] + start + s[index+1:]

def swap2(s, i):
    # binary search solution
    pass
