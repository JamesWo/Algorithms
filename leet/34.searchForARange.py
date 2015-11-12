"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """ 
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        lo = 0 
        hi = len(nums)-1
        while lo < hi: 
            mid = lo + (hi-lo)/2
            if nums[mid] < target:
                lo = mid+1
            else:
                hi = mid 
        if nums[lo] != target:
            ret.append(-1)
        else:
            ret.append(lo)
               
        lo = 0 
        hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo+1)/2
            if nums[mid] > target:
                hi = mid-1
            else:
                lo = mid
        if nums[lo] != target:
            ret.append(-1)
        else:
            ret.append(lo)
        return ret
                  
