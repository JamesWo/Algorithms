from stack import *

class queue(object):
    pushStack = stack()
    popStack = stack()
    
    def push(self, item):
        while not self.popStack.isempty():
            self.pushStack.push(self.popStack.pop())
        self.pushStack.push(item)

    def pop(self):
        if self.isempty():
            return False
        while not self.pushStack.isempty():
            self.popStack.push(self.pushStack.pop())
        return self.popStack.pop()

    def isempty(self):
        return self.pushStack.isempty() and \
                self.popStack.isempty()

# test

q = queue()
assert q.isempty()
q.push(1)
assert not q.isempty()
q.push(2)
assert not q.isempty()
assert q.pop() == 1
assert not q.isempty()
assert q.pop() == 2
assert q.isempty()
