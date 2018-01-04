from Tree import Tree

tree = Tree()

tree.insert(1)
tree.insert(222)
tree.insert(32)
tree.insert(4)
tree.insert(5)

tree.traverseInOrder()

print("-----------------------")
tree.remove(1)
tree.traverseInOrder()
