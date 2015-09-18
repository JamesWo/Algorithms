#https://www.hackerrank.com/challenges/acm-icpc-team
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
def pairExists(n, people, countPairs=False):
    """ Returns whether there exists a pair of people
    whose combined known topics >= n.
    If countPairs, return the number of pairs that
    have combined known topics >= n.
    """
    count = 0
    for x, y in itertools.combinations(range(len(people)), 2):
        if bin(people[x] | people[y]).count('1') >= n:
            if not countPairs:
                return True
            else:
                count += 1
    return count if countPairs else False
    
numPeople, numTopics = map(int, raw_input().split(" "))
people = []
for _ in range(numPeople):
    people.append(int(raw_input(), 2))
# binary search for the max topics known
lo = 0
hi = numTopics
while lo < hi:
    mid = lo + (hi - lo + 1)/2
    if pairExists(mid, people) > 0:
        lo = mid
    else:
        hi = mid - 1
        
print lo
print pairExists(lo, people, countPairs=True)

