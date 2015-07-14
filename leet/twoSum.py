class Solution:
    def twoSum(self, nums, target):
        nums.sort()
        if not nums or len(nums)<2:
            print "F1"
            return False
        head = 0
        tail = 1
        print head,tail
        while head < tail:
            while tail < (len(nums)-1) and (nums[head] + nums[tail+1]) < target:
                tail += 1
                print head,tail
            if nums[head] + nums[tail] == target:
                print "RESULT %d   %d" % (head+1,tail+1)
                return [ head+1, tail+1 ]
            head += 1
            print head,tail
        print "F2"
        return False

# test
# assumptions:
#   a single solution always exists
s = Solution()
assert s.twoSum([5,7],12) == [1,2]
assert s.twoSum([5,7,10],12) == [1,2]
assert s.twoSum([1, 3, 5,7,10],12) == [3,4]


