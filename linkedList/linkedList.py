# singly linked list

class node(object):
    value = None
    next = None
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

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






