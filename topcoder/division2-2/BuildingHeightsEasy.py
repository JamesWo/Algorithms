def minimum(M, heights):
    optimal = 51*51
    heights.sort(reverse=True)
    for h in range(51):
        if len( filter(lambda x: x<=h, heights) ) < M:
            continue
        # compute how many floors we need to add to get M buildings of height h
        finished = 0
        cost = 0
        for building in heights:
            if finished >= M:
                break
            if building > h:
                continue
            elif building == h:
                finished += 1
            else:
                finished += 1
                cost += ( h - building )
        assert finished == M
        if cost < optimal:
            optimal = cost
    return optimal

