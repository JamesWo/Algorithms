# Enter your code here. Read input from STDIN. Print output to STDOUT
def maxTasks(tasks, time):
    totalTime = 0
    count = 0
    for task in tasks:
        totalTime += task
        if totalTime > time:
            return count
        count += 1
    return count

case = 1
while True:
    try:
        line1 = raw_input()
        line2 = raw_input()
    except EOFError:
        break
    n, t = map(int, line1.split(" "))
    tasks = map(int, line2.split(" "))
    print "Case %d: %d" % (case, maxTasks(tasks, t))
    case += 1
