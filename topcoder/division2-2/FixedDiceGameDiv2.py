def getExpectation(a, b):
    wins = []
    for i in range(1, a+1):
        for j in range(1, b+1):
            if i > j:
                wins.append(i)
    return 1.0*sum(wins) / len(wins)
