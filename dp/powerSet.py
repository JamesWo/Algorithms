import sets

def setCopy(s):
    new = set()
    for elem in set:
        new.add(elem)

def powerSet(lst):
    """ returns the power set of the list lst """
    ret = []
    if not lst:
        return [ret]
    elem = lst[0]
    remaining = powerSet(lst[1:])
    for sublist in remaining:
        new = [elem] + sublist # makes a copy
        ret.append(new)
        ret.append(sublist)
    return ret

# test
inp = [1,2,3] 
out = [ [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] ]
result = powerSet(inp)
for elem in result:
    assert elem in out, elem
for elem in out:
    assert elem in result, elem
