# returns kth last element from linked list
import sys
sys.path.append('..')
from linkedList import *

def kth(node, k):
    length = 0
    curr = node
    while curr:
        length += 1
        curr = curr.next

    while length > k:
        length -= 1
        node = node.next

    return node

l = createLinkedList([1,2,3,4,5])
node = kth(l, 1)
assert node.value == 5
node = kth(l, 2)
assert node.value == 4
node = kth(l, 5)
assert node.value == 1
