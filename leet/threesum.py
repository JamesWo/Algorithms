import collections

class Solution(object):
    def twoSum(self, numbers, n):
        result = set()
        for i in numbers:
            if numbers[i] <= 0:
                continue
            numbers[i] -= 1
            # we want n + i + x = 0 ==> x = -(n+i) 
            if numbers[-n-i] > 0:
                result.add(tuple(sorted([n, -n-i, i])))
            numbers[i] += 1
        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = collections.Counter()
        for n in nums:
            s[n] += 1
        result = self.threeSumSet(s)
        return [[x for x in t] for t in result]

    def threeSumSet(self, numbers):
        result = set()
        for i in numbers:
            numbers[i] -= 1
            result = result.union(self.twoSum(numbers, i))
            numbers[i] += 1
        return result

assert Solution().threeSum([1,1,-2]) == [[-2,1,1]] 
        
