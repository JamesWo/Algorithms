#
# reverse a linked-list
from linkedList import *

def reverse(lst):
    if not lst.head or not lst.head.next:
        return lst
    prev = None
    p1 = lst.head
    while p1:
        n1 = p1.next
        p1.next = prev
        prev = p1
        p1 = n1
    lst.head = prev
    return

lst = linkedList()
lst.insertFront(3)
lst.insertFront(2)
lst.insertFront(1)

assert lst.__str__() == '1, 2, 3'
reverse(lst)
assert lst.__str__() == '3, 2, 1'

lst.insertBack(5)
lst.insertBack(4)

assert lst.__str__() == '3, 2, 1, 5, 4'
reverse(lst)
assert lst.__str__() == '4, 5, 1, 2, 3'

print 'pass'
