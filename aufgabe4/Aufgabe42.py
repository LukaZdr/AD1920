########## Unterstützender Code ##########
class Node:
    def __init__(self):
        self.key = None
        self.parent = None
        self.left = None
        self.right = None

########## Lösung ##########

# Node in parameter represents root of tree
def delete(root, delete):
    #TODO Student
    return None

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
root.left = Node()
root.left.key = 1
root.left.parent = root
root.right = Node()
root.right.key = 3
root.right.parent = root
# Call delete
root = delete(root, root.right)

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
root.left = Node()
root.left.key = 1
root.left.parent = root
root.right = Node()
root.right.key = 3
root.right.parent = root
root.right.right = Node()
root.right.right.key = 99
root.right.right.parent = root.right

# Call delete
root = delete(root, root.right)

# Compare
NewRoot = Node()
NewRoot.key = 2
NewRoot.left = Node()
NewRoot.left.key = 1
NewRoot.left.parent = NewRoot
NewRoot.right = Node()
NewRoot.right.key = 99
NewRoot.right.parent = NewRoot

if compare_trees(root, NewRoot):
    print("Test 2: Success")
else:
    print("Test 2: Failure")

### Test 3
# build tree
root = Node()
root.key = 2
root.left = Node()
root.left.key = 1
root.left.parent = root
root.right = Node()
root.right.key = 50
root.right.parent = root
root.right.right = Node()
root.right.right.key = 99
root.right.right.parent = root.right
root.right.left = Node()
root.right.left.key = 25
root.right.left.parent = root.right

# Call delete
root = delete(root, root.right)

# Compare
newRoot = Node()
newRoot.key = 2
newRoot.left = Node()
newRoot.left.key = 1
newRoot.left.parent = newRoot
newRoot.right = Node()
newRoot.right.key = 99
newRoot.right.parent = newRoot
newRoot.right.left = Node()
newRoot.right.left.key = 25
newRoot.right.left.parent = newRoot.right

if compare_trees(root, newRoot):
    print("Test 3: Success")
else:
    print("Test 3: Failure")