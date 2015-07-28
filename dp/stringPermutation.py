import sets
import pdb

def stringToCounts(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

class generatePerms(object):
#    self.perms = None
    def getPerms(self, s):
        """
        return a set of all permutations of the characters in the string s.
        """
        self.perms = set()
        self.getPermsHelper(stringToCounts(s))
        return self.perms
    def getPermsHelper(self, d):
        ret = set()
        newPerms = set()
        for c in d.keys():
            if d[c]==1:
                d.pop(c)
                newPerms = self.getPermsHelper(d)
                d[c] = 1
            else:
                d[c] -= 1
                newPerms = self.getPermsHelper(d)
                d[c] += 1
            ret.add( c )
            for string in newPerms:
                ret.add( c + string )
        self.perms.update(ret)
        return ret


# test
inp = "cbfc"
expected = set(["cbfc", "cbcf", "ccbf", "ccfb", "cfbc", "cfcb", "bccf", "bcfc", "bfcc", "fbcc", "fcbc", "fccb", "cbf", "cfb", "bcf", "bfc", "bcc", "fcb", "fbc", "fcc", "cfc", "ccf", "ccb", "cbc", "cc", "cb", "bc", "cf", "fc", "bf", "fb", "c", "b", "f"])
result = generatePerms().getPerms(inp)
assert result == expected



