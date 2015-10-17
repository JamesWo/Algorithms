"""
Given a sorted array and a target value, return the index 
if the target is found.  If not, return the index where 
it would be if it were inserted in order.
"""

class Solution:
    def builtinInsert(self, arr, target):
        return arr.insort(target)

    def searchInsert(self, arr, target):
        for i in range(len(arr)):
            if arr[i] >= target:
                return i
        return len(arr)

    def binarySearchInsert(self, arr, target):
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = (lo + hi)/2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

# test code
inp = [3,5,8,13,18,23]
inp2 = [1,3,5,6]
s = Solution()
for i in range(len(inp)):
    assert s.searchInsert(inp, inp[i])==i
    assert s.searchInsert(inp, inp[i]+1) == i+1
    assert s.binarySearchInsert(inp, inp[i])==i
    assert s.searchInsert(inp2, 7) == 4
    assert s.binarySearchInsert(inp2, 7)==4

print "all test passed"
