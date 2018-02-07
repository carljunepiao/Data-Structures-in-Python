from tree import BalancedTree
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

tree = BalancedTree()
tree.insert(6)
tree.insert(3)
tree.insert(4)


tree.traverseInOrder()

logging.info("--------------------------------------------------------------")
print("Done")
