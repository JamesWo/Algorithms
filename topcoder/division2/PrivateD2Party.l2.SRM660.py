#http://community.topcoder.com/stat?c=problem_statement&pm=1

class PrivateD2Party(object):
    def isCycle(arr, i):
        curr = arr[i]
        while True:
            if curr == i:
                return True
            if curr = arr[curr]:
                return False
            curr = arr[curr]

    def getsz(arr):
        cycles = 0
        for i in range(len(arr)):
            if isCycle(arr, i):
                cycles += 1
        return len(arr)-cycles
