########## Unterstützender Code ##########
class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None

########## Lösung ##########

# Node in parameter represents root of tree
def insert(root, insert):
	current_node = root
	last_node = None

	while current_node != None:
		last_node = current_node
		if insert.key < current_node.key:
			current_node = current_node.left
		else:
			current_node = current_node.right

	insert.parent = last_node

	if last_node == None:
		root = insert
	elif insert.key < last_node.key:
		last_node.left = insert
	else:
		last_node.right = insert
	return root

########## Tests ##########
def compare_trees(m, n):
    # None check
    if n is None and m is None:
        return True
    if n is not None and m is None:
        return False
    if n is None and m is not None:
        return False

    # Root
    if n.parent is None and m.parent is not None:
        return False
    if n.parent is not None and m.parent is None:
        return False
    if n.parent is not None and m.parent is not None:
        if n.parent.key != m.parent.key:
            return False

    # Key
    if m.key != n.key:
        return False

    # Left side
    if n.left is None and m.left is not None:
        return False
    if n.left is not None and m.left is None:
        return False
    if n.left is not None and m.left is not None:
        if not compare_trees(n.left, m.left):
            return False

    # Right side
    if n.right is None and m.right is not None:
        return False
    if n.right is not None and m.right is None:
        return False
    if n.right is not None and m.right is not None:
        if not compare_trees(n.right, m.right):
            return False

    # Correct parents
    if n.right is not None:
        if n.right.parent is not n:
            return False

    if n.left is not None:
        if n.left.parent is not n:
            return False

    if m.right is not None:
        if m.right.parent is not m:
            return False

    if m.left is not None:
        if m.left.parent is not m:
            return False

    # All passed
    return True

### Test 1
# build tree
root = Node()
root.key = 2

# build target
target = Node()
target.key = 1

# Call insert
root = insert(root, target)

# Compare
NewRoot = Node()
NewRoot.key = 2
NewRoot.left = Node()
NewRoot.left.key = 1
NewRoot.left.parent = NewRoot

if compare_trees(root, NewRoot):
    print("Test 1: Success")
else:
    print("Test 1: Failure")

### Test 2

# build tree
root = Node()
root.key = 2

# build target
target = Node()
target.key = 3

# Call insert
root = insert(root, target)

# Compare
NewRoot = Node()
NewRoot.key = 2
NewRoot.right = Node()
NewRoot.right.key = 3
NewRoot.right.parent = NewRoot

if compare_trees(root, NewRoot):
    print("Test 2: Success")
else:
    print("Test 2: Failure")