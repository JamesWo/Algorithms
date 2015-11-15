class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def iter1(self):
        if self.left:
            for x in self.left.iter1():
                yield x
        yield self.val
        if self.right:
            for x in self.right.iter1():
                yield x

#test
#         3
#       /  \ 
#      2    5
#          / \
#         4   8
#
root = node(3)
root.left = node(2)
root.right = node(5)
root.right.left = node(4)
root.right.right = node(8)

i = root.iter1()
result = list(i)
assert result == [2,3,4,5,8]

#import pdb; pdb.set_trace()
#print 1
