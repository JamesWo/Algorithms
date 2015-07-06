import sys
sys.path.append('..')
from linkedList import *

# recursive implementation

def lladd(head1, head2):
    return helper(head1, head2, 0)

def helper(node1, node2, carry):
    if not (node1 or node2 or carry):
        return None
    if node1:
        carry += node1.value
        node1 = node1.next
    if node2:
        carry += node2.value
        node2 = node2.next

    newNode = node(carry % 10, helper(node1, node2, 1 if carry>9 else 0))
    return newNode


# test functions

def createNumber(n):
    nstr = str(n)
    head = node(int(nstr[0]))
    for char in nstr[1:]:
        newNode = node(int(char), head)
        head = newNode
    return head

# test createNumber
assert createNumber('159').__str__() == '9, 5, 1'

# make two ll numbers and add them
l1 = createNumber(123)
l2 = createNumber(45)
sumlist = lladd(l1, l2)
assert sumlist.__str__() == '8, 6, 1'

num1 = 987
num2 = 8765
l1 = createNumber(num1)
l2 = createNumber(num2)
sumlist = lladd(l1, l2)
assert sumlist.__str__() == '2, 5, 7, 9'
