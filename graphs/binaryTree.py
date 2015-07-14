import random

class node(object):
    left = None
    right = None
    data = None
	

def createBalanced(depth=1):
    if depth == 0:
	return None
    root = node()
    root.left = createBalanced(depth = depth-1)
    root.right = createBalanced(depth = depth - 1)
    root.data = random.randint(0, 100)
    return root


