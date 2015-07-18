# http://community.topcoder.com/stat?c=problem_statement&pm=13881

class ExactTreeEasy(object):
    def getTree(self, nodes, leaves):
        result = []
        for i in range(nodes-leaves+1):
            result.append(i)
            result.append(i+1)
        appendTo = 1
        for j in range(nodes-leaves+2, nodes):
            result.append(appendTo)
            appendTo += 1
            result.append(j)
        return result

tester = ExactTreeEasy()

# There are too many correct solutions for each test.  I am too lazy to implement a real test...
inp = [
(4,2),
(4,3),
(3,2),
(5,3),
(10,9)
        ]

for case in inp:
    print "input: %s" % str(case)
    print "output: %s" % tester.getTree(*case)
