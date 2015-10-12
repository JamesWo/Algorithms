"""
Given a set of candidate numbers C, and a target
numer T, find all unique combinations in C where the candidate
numbers sum to T.

The same repeated number ay be chosen from C
unlimited number of times.

All numbers will be positive integers

Elements in combination must be in non-descending order.

The solution set must not contain duplicate combinations.
"""

class Solution:
    def combinations(self, C, target):
        return self.combinations_(sorted(list(set(C))), target, len(C)-1)

    def combinations_(self, C, target, i):
        result = []
        if len(C) == 0:
            return result
        while i >= 0:
            num = C[i]
            if num == target:
                result.append([num])
            elif num < target:
                for res in self.combinations_(C, target-num, i):
                    result.append(res + [num])
            i -= 1
        return result

# test
s = Solution()
assert (7,) in set(map(tuple, s.combinations([2,3,6,7], 7)))
assert (2,2,3) in set(map(tuple, s.combinations([2,3,6,7], 7)))
print "test passed"
