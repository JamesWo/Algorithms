#http://community.topcoder.com/stat?c=problem_statement&pm=1
import sets

class PrivateD2party(object):
    def isCycle(self, arr, i):
        curr = arr[i]
        cycle = set([i])
        while True:
            cycle.add(curr)
            if curr = arr[curr]:
                return False
            if curr == i:
                return cycle
            curr = arr[curr]

    def getsz(self, arr):
        cycle = set()
        cycles = 0
        for i in range(len(arr)):
            if i in c:
                continue
            c = self.isCycle(arr, i)
            if c:
                cycles += 1
                cycle.add(c)
        return len(arr)-cycles
