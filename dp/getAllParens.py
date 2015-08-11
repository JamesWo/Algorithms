def getParensHelper(s, n, opened, partial):
    if len(partial) == 2*n:
        s.append( "".join( partial ) )
    elif opened == n:
        new = partial[:]
        while len(new) < 2*n:
            new.append( ")" )
        s.append( "".join( new ) )
    else:
        if opened > 0:
            copy = partial[:]
            copy.append( ")" )
            getParensHelper( s, n, opened-1, copy )
        if opened < n and ( 2*n - len( partial ) - 1) >= ( opened + 1 ):
            copy = partial[:]
            copy.append( "(" )
            getParensHelper( s, n, opened+1, copy)
    return s

def getAllParens(n):
    ans = []
    return getParensHelper(ans, n, 0, [])


# test

expected = [
        '()()',
        '(())',
        ]

assert set(getAllParens( 2 )) == set(expected)

expected = [
        '((()))',
        '(()())',
        '()()()',
        '()(())',
        '(())()',
        ]

assert set(getAllParens( 3 )) == set(expected)
