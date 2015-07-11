#A stack of integers which supports O(1) finding min element
import numbers

class _stack_node(object):
    item = None
    nxt = None
    def __init__(self, item, nxt):
	self.item = item
	self.nxt = nxt

class stack(object):
    # maintain a stack of min elements
    minElements = None

    head = None
    def push(self, item):
	assert isinstance(item, numbers.Real), "stack only supports integers"
	self.head = _stack_node(item, self.head)
	if not self.minElements or item < self.minElements.item:
	    self.minElements = _stack_node(item, self.minElements)
	
    def pop(self):
	assert not self.isempty(), "Cannot pop from empty stack"
	item = self.head.item
	self.head = self.head.nxt
	if self.minElements and item == self.minElements.item:
	    self.minElements = self.minElements.nxt
	return item

    def minitem(self):
	if not self.minElements:
	    return None
	return self.minElements.item

    def isempty(self):
	return self.head is None

# test
s = stack()
assert s.isempty()
assert s.minitem() == None
s.push(3)
assert s.minitem() == 3
assert not s.isempty()
s.push(5)
assert s.minitem() == 3
s.push(1)
assert s.minitem() == 1

s.push(7.5)
assert s.minitem()==1
assert s.pop() == 7.5
s.push(0.5)
assert s.minitem() == 0.5
assert s.pop() == 0.5

s.pop()
assert s.minitem() == 3
assert s.pop() == 5
assert s.minitem() == 3
assert not s.isempty()
assert s.pop() == 3
assert s.minitem() == None
assert s.isempty()


