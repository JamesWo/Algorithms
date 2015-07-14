from binaryTree import *

def isBalanced(root):
    def isBalHelper(node):
	""" returns (bool, int) tuple where
	    bool == True iff subtree under node is balanced,
	    int = if balanced, number of nodes in subtree under node (including node)
		  if not balanced, int = 0
	"""
	if not node.left and not node.right:
	    return (True, 1)
	if not node.left or not node.right:
	    return (False, 0)
	balLeft, sizeLeft = isBalHelper(node.left)
	balRight, sizeRight = isBalHelper(node.right)
	if not ( balLeft and balRight and sizeLeft == sizeRight ):
	    return (False, 0)
	return (True, sizeLeft+sizeRight+1)		    
    return isBalHelper(root)[0]

binaryTree = createBalanced(depth=5)
assert isBalanced(binaryTree)

mid = binaryTree.left.right.left
mid.right = None

assert not isBalanced(binaryTree)
