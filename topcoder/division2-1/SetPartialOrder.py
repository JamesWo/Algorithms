"""
https://community.topcoder.com/stat?c=problem_statement&pm=14075
"""

class SetPartialOrder:
    def compareSets(self, lst1, lst2):
        s1 = set(lst1)
        s2 = set(lst2)
        if s1 == s2:
            return "EQUAL"
        elif s1 < s2:
            return "LESS"
        elif s1 > s2:
            return "GREATER"
        else:
            return "INCOMPARABLE"


