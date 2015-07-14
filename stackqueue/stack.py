#basic stack data structure, implemented using a linked list

class _stack_node(object):
    item = None
    nxt = None
    def __init__(self, item, nxt):
	self.item = item
	self.nxt = nxt

class stack(object):
    head = None
    def push(self, item):
	self.head = _stack_node(item, self.head)

    def pop(self):
	assert not self.isempty(), "Cannot pop from empty stack"
	item = self.head.item
	self.head = self.head.nxt
	return item

    def isempty(self):
	return self.head is None

    def peek(self):
        if self.head:
            return self.head.item
        return None

# test
s = stack()
assert s.isempty()
s.push(3)
assert not s.isempty()
s.push(5)
assert s.peek() == 5
assert s.pop() == 5
assert not s.isempty()
assert s.pop() == 3
assert s.isempty()
assert s.peek() == None
