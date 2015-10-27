# Enter your code here. Read input from STDIN. Print output to STDOUT
def agree(lst1, lst2):
    order1 = map(lambda x:x[0], sorted(enumerate(lst1), key=lambda x:x[1], reverse=True))
    order2 = map(lambda x:x[0], sorted(enumerate(lst2), key=lambda x:x[1], reverse=True))
    for i in range(len(order1)):
        if order1[i] != order2[i]:
            return str(i+1)
    return "agree"


currList = []
case = 1
n = 0
while True:
    try:
        inp = raw_input()
    except EOFError:
        print "Case %d: %s" % (case, agree(currList[:n], currList[n:]))
        break
    if not inp:
        continue
    nums = map(int, inp.split())
    for num in nums:
        if len(currList) == 2*n:
            if n > 0:
                print "Case %d: %s" % (case, agree(currList[:n], currList[n:]))
                case += 1
            currList = []
            n = num
        else:
            currList.append(num)


