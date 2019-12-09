from binarytree import tree

mytree = tree(height=5)

print(mytree)


def getDepth(tree):
  return NodeDepth(tree) - 1

def NodeDepth(tree):
  if tree == None: return 0
  return max(NodeDepth(tree.left), NodeDepth(tree.right)) + 1

print(getDepth(mytree))
