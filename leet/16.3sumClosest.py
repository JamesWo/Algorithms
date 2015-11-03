import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums)<3:
            assert False, "no solution"
        nums.sort()
        bestSum = None
        bestCost = sys.maxint
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                currSum = nums[i] + nums[left] + nums[right]
                diff = abs(target - currSum)
                if diff < bestCost:
                    bestCost = diff
                    bestSum = currSum
                if currSum > target:
                    right -= 1
                else:
                    left += 1
        assert bestSum is not None, "no solution found"
        return bestSum

#test
s = Solution()
assert s.threeSumClosest([1,2,4,8,16,32,64,128], 82) == 82
