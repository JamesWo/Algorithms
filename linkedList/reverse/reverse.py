#reverse linked list

from linkedList import *
import random

def reverse(head):
    if head is None:
        return None
    if not isinstance(head, node):
        assert False
    prev = head
    curr = head.next
    nextNode = None
    head.next = None
    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev

NUMCASES = 1000
for _ in range(NUMCASES):
    lst = [random.randint(0,100) for i in range(random.randint(0,30))]
    ll = createLinkedList(lst)
    reversedll = createLinkedList(lst[::-1])
    assert reverse(ll).__str__() == reversedll.__str__()

