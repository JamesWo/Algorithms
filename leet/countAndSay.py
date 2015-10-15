"""
The count-and-say sequence is the sequence of integers begining 
as follows.
1, 11, 21, 1211, 111221.
Given an integer 1, generate the nth sequence.
"""
def convertStrs(lastSeen, lastCount):
    """
    @param lastSeen: a string representing a integer
    @param lastCount: an integer, how many times of lastSeen
    @return: list of single-character strings
    """
    result = []
    for char in str(lastCount):
        result.append(char)
    for char in lastSeen:
        result.append(char)
    return result

class Solution:
    def nthSeq(self, n):
        return int("".join(self.nthSeq_(n)))
    def nthSeq_(self, n):
        """
        @param n: integer of the sequence number required
        @return: List of strings representing the sequence
        """
        if n == 1:
            return ["1"]
        seq = self.nthSeq_(n-1)
        ret = []
        index = 0
        lastSeen = None
        lastCount = 0
        while index < len(seq):
            if seq[index] == lastSeen:
                lastCount += 1
            else:
                if lastSeen is not None:
                    ret.extend(convertStrs(lastSeen, lastCount))
                lastSeen = seq[index]
                lastCount = 1
            index += 1
        if lastSeen is not None:
            ret.extend(convertStrs(lastSeen, lastCount))
        return ret

#test
s = Solution()
assert s.nthSeq(1) == 1
assert s.nthSeq(2) == 11
assert s.nthSeq(3) == 21
assert s.nthSeq(4) == 1211
assert s.nthSeq(5) == 111221
assert s.nthSeq(6) == 312211
assert s.nthSeq(7) == 13112221
assert s.nthSeq(8) == 1113213211
assert s.nthSeq(9) == 31131211131221
assert s.nthSeq(10) == 13211311123113112211
