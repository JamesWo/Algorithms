from stack import *

def sortStack(s):
    newStack = stack()
    while not s.isempty():
        top = s.pop()
        counter = 0
        while not newStack.isempty() and newStack.peek() < top:
            counter += 1
            s.push(newStack.pop())
        newStack.push(top)
        while counter > 0:
            newStack.push(s.pop())
            counter -= 1
    return newStack




# test

s = stack()
s.push(3)
s.push(7)
s.push(5)

sortedStack = sortStack(s)
assert sortedStack.pop() == 3
assert sortedStack.pop() == 5
assert sortedStack.pop() == 7
assert sortedStack.isempty()

