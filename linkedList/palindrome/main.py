# checks whether a linked list, represented by a head node, is a palindrome

import sys
sys.path.append('..')
from linkedList import *

def isPalindrome(head):
    ptr = head
    reverse = None
    while ptr:
	reverse = node(ptr.value, reverse)
	ptr = ptr.next
    while head or reverse:
	if head.value != reverse.value:
	    return False
	head = head.next
	reverse = reverse.next
    return True



# test

palindromes = []
palindromes.append(createLinkedList( [1, 2, 3, 2, 1]))
palindromes.append(createLinkedList( [2, 2, 3, 2, 2]))
palindromes.append(createLinkedList( [3, 3, 3, 3, 3]))
palindromes.append(createLinkedList( [3, 3, 3, 3]))
palindromes.append(createLinkedList( [3, 5, 5, 3]))
palindromes.append(createLinkedList( [3, 3]))
palindromes.append(createLinkedList( [3]))
palindromes.append(createLinkedList( []))

notpalindromes = []
notpalindromes.append(createLinkedList( [1, 2, 3, 2, 2]))
notpalindromes.append(createLinkedList( [2, 2, 3, 3, 2]))
notpalindromes.append(createLinkedList( [3, 3, 3, 3, 1]))
notpalindromes.append(createLinkedList( [3, 4, 3, 3]))
notpalindromes.append(createLinkedList( [3, 6, 5, 3]))
notpalindromes.append(createLinkedList( [3, 6]))

def printError(l, check):
    print l,
    print "is %sa palindrome" % ( "not " if check else "" )
    return ""

for l in palindromes:
    assert isPalindrome(l), printError(l, True)

for l in notpalindromes:
    assert not isPalindrome(l), printError(l, False)

print "Pass"
