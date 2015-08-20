def canItBeDone(k, A):
    for i in range(1, len(A)+1):
        if A.count(i) == 0:
            return "IMPOSSIBLE"
        if A.count(i) == 1:
            continue
        if A.count(i) > 1:
            # add k to all but one of them
            found = False
            for index in range(len(A)):
                if A[index] == i:
                    if not found:
                        found = True
                        continue
                    else:
                        A[index] += k
    return "POSSIBLE"
