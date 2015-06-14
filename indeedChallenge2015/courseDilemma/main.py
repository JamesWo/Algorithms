#https://www.hackerrank.com/contests/indeed-prime-challenge/challenges/course-dilemma

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sets

numCases = input()

debugMode = False
def log(obj):
    if debugMode:
        print obj

def solve():
    numCourses, numRelations = map(int, raw_input().split(" "))
    relations = { i:set() for i in range(numCourses) }
    for i in range(numRelations):
        prereq, course = map(int, raw_input().split(" "))
        relations[course].add(prereq)
    log(relations)
    
    numIter = 0
    completedCourses = set()
    while(True):
        completedCourses = set()
        if not relations:
            return numIter
        numIter += 1
        for course, prereqs in relations.iteritems():
            if not prereqs:
                completedCourses.add(course)
        found=False
        for course in completedCourses:
            del relations[course]
            found=True
        if not found:
            return False
        for prereqs in relations.itervalues():
            for c in completedCourses:
                prereqs.discard(c)
        log(relations)
        log(completedCourses)
            
                


for caseNum in range(1, numCases+1):
    result = solve()
    print "Case %d:" % caseNum,
    if result is False:
        print "Never Ends"
    else:
        print "%d semester(s)" % result




