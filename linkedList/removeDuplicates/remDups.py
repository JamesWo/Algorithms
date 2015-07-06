# remove duplicates in a singly-linked list

import sys
sys.path.append('..')
from linkedList import *

import sets

def remDups(node):
    seen = set()
    prev = node
    curr = node
    while curr:
        if curr.value in seen:
            curr = curr.next
            prev.next = curr
        else:
            seen.add(curr.value)
            prev = curr
            curr = curr.next
    return node


# test
l = createLinkedList([1,2,3,4,5,1,3, 6])
print l # should print 1, 2, 3, 4, 5, 1, 3, 6
l = remDups(l)
print l # should print 1, 2, 3, 4, 5,6
assert l.__str__() == '1, 2, 3, 4, 5, 6'

l = createLinkedList([1,1,1])
print l
l = remDups(l)
print l
assert l.__str__() == '1'
