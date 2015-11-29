"""
https://community.topcoder.com/stat?c=problem_statement&pm=14062
"""
class Cdgame:
    def rescount(self, lst1, lst2):
        sum1 = sum(lst1)
        sum2 = sum(lst2)
        possible = set()
        for num1 in lst1:
            for num2 in lst2:
                possible.add((sum1 + num2 - num1) * (sum2 + num1 - num2))
        return len(possible)


#test
testCases = [
[[1,2],[3,4],2],
[[1,2,4],[8,16,32],9],
[[1,1,1],[1,1,1],1],
[[1,2,3],[5,5,5],3],
[[3,3,4,1],[2,2,2,100],4],
[[31,34,55,56,57],[1,2,3,4,5],15]
]

tester = Cdgame()
for lst1, lst2, expectedOutput in testCases:
    if tester.rescount(lst1, lst2) != expectedOutput:
        print "Test case failed.  ", lst1, lst2, expectedOutput, tester.rescount(lst1, lst2)
        assert False

