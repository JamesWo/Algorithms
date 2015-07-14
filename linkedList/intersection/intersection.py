import sys
sys.path.append('..')
from linkedList import *

def intersection(node1, node2):
    tail1 = node1
    len1 = 0
    while tail1:
        tail1 = tail1.next
        len1 += 1

    tail2 = node2
    len2 = 0
    while tail2:
        tail2 = tail2.next
        len2 += 1
    if tail1 is not tail2:
        return False

    while len1 > len2:
        len1 -= 1
        node1 = node1.next
    while len2 > len1:
        len2 -= 1
        node2 = node2.next
    while True:
        if node1 is node2:
            return node1
        node1 = node1.next
        node2 = node2.next
    assert False, 'unreachable'



# test

list1 = createLinkedList([1,2,3])
list2 = createLinkedList([2,3,4])
assert intersection(list1, list2) is None

tail2 = list2.next.next
assert tail2.value == 4
list1mid = list1.next
assert list1mid.value == 2
tail2.next = list1mid
assert intersection(list1, list2) is list1mid


