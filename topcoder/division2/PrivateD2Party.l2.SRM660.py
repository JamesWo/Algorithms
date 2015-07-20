#http://community.topcoder.com/stat?c=problem_statement&pm=1
import sets

class PrivateD2party(object):
    def isCycle(self, arr, i):
        curr = arr[i]
        cycle = set([i])
        while True:
            cycle.add(curr)
            if curr == arr[curr]:
                return False
            if arr[curr] == i:
                return cycle
            if curr in cycle:
                return False
            curr = arr[curr]

    def getsz(self, arr):
        cycle = set()
        cycles = 0
        for i in range(len(arr)):
            if i in cycle:
                continue
            c = self.isCycle(arr, i)
            if c:
                cycles += 1
                cycle= cycle.union(c)
        return len(arr)-cycles

tester = PrivateD2party()
result = tester.getsz( [5,2,2,4,5,0] )
assert result == 5

result = tester.getsz( [1,0,3,2] )
assert result == 2
