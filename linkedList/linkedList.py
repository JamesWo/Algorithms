# singly linked list

# super simple node object.
class node(object):
    value = None
    next = None
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
	
    def __str__(self):
        retStr = []
        ptr = self
        while ptr:
            retStr.append(ptr.value)
            ptr = ptr.next
        return ", ".join(map(str,retStr))
    
# create a linkedList given a python list l
# returns head node
def createLinkedList(l):
    if not l:
        return None
    head = None
    for i in reversed(l):
        head = node(i, head)
    return head

def testNode():
    n = node(3)
    assert n.__str__() == '3'
    n = node(4, n)
    assert n.__str__() == '4, 3'
    # test createLinkedList
    assert createLinkedList([]) == None
    assert createLinkedList([1]).__str__() == '1'
    assert createLinkedList([1,3,2]).__str__() == '1, 3, 2'

    print 'pass'

# a wrapper for a linkedList object
# most of the time, this will not be used, and we will
# just say a node object representing the head is the LL
class linkedList(object):
    head = None
    length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        headPtr = self.head
        retStr = []
        while headPtr:
            retStr.append(headPtr.value)
            headPtr = headPtr.next
        return ", ".join(map(str,retStr))
            
    def insertFront(self, value):
        if self.head:
            newNode = node(value, self.head)
            self.head = newNode
        else:
            self.head = node(value)
        self.length += 1

    def insertBack(self, value):
        if not self.head:
            self.head = node(value)
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.next = node(value)
        self.length += 1

    def removeFront(self):
        if not self.head:
            return None
        ret = self.head.value
        self.head = self.head.next
        self.length -= 1
        return ret

    def removeBack(self):
        if not self.head:
            return None
        self.length -= 1
        if not self.head.next:
            ret = self.head.value
            self.head = None
            return ret
        secondLast = self.head
        while secondLast.next.next:
            secondLast = secondLast.next
        ret = secondLast.next.value
        secondLast.next = None
        return ret




def testLinkedList():
    l = linkedList()
    assert len(l) == 0
    assert not l.head
    assert l.__str__() == ""
    assert not l.removeFront()
    assert not l.removeBack()
    assert len(l) == 0
    l.insertFront(2)
    assert len(l)==1
    l.insertFront(3)
    assert len(l)==2
    assert l.__str__() == "3, 2"
    assert 2 == l.removeBack()
    assert len(l)==1
    assert l.__str__() == "3"
    assert 3 == l.removeFront()
    assert len(l) == 0
    assert not l.head
    print "pass"






