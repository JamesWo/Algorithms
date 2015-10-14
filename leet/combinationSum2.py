"""
Given a set of candidate numbers C, and a target
numer T, find all unique combinations in C where the candidate
numbers sum to T.

An element of C can only be chosen once per combination.

All numbers will be positive integers

Elements in combination must be in non-descending order.

The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinations(self, C, target):
        return self.combinations_(sorted(C), target, len(C)-1)

    def combinations_(self, C, target, i):
        result = []
        if len(C) == 0:
            return result
        while i >= 0:
            num = C[i]
            if num == target:
                result.append([num])
            elif num < target:
                for res in self.combinations_(C, target-num, i-1):
                    result.append(res + [num])
            i -= 1
        return result

# test
s = Solution()
result = set(map(tuple, s.combinations([2,3,6,7], 7)))
assert len(result) == 1
assert (7,) in result
assert (2,2,3) not in result

result = set(map(tuple, s.combinations([10,1,2,7,6,1,5])))
assert len(result)==4
assert (1,7) in result
assert (1,2,5) in result
assert (2,6) in result
assert (1,1,6) in result

print "test passed"
