def playList(n):
    res = []
    for i in range(1,n+1):
        res.append( "%d.mp3" % i )
    res.sort()
    if len(res) > 50:
        res = res[0:50]
    return res
