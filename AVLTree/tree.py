from Node import Node
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class BalancedTree():
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        parentNode = self.rootNode

        if self.rootNode == None:
            parentNode = Node(data, None)
            self.rootNode = parentNode
        else:
            parentNode = self.rootNode.insert(data, self.rootNode)

        self.rebalanceTree(parentNode)

    def rebalanceTree(self, parentNode):
        self.setBalance(parentNode)

        if parentNode.balance <= -1:
            if self.getHeight(parentNode.leftChild.leftChild) >= self.getHeight(parentNode.leftChild.rightChild):
                parentNode = self.rotateRight(parentNode)
            else:
                parentNode = self.rotateLeftRight(parentNode)
        elif parentNode.balance > 1:
            if self.getHeight(parentNode.rightChild.rightChild) >= self.getHeight(parentNode.rightChild.leftChild):
                parentNode = self.rotateLeft(parentNode)
            else:
                parentNode = self.rotateRightLeft(parentNode)

        if parentNode.parentNode is not None:
            self.rebalanceTree(parentNode.parentNode)
        else:
            self.rootNode = parentNode

    def traverseInOrder(self):
        self.rootNode.traverseInOrder()

    def setBalance(self, node):
        node.balance = (self.getHeight(node.rightChild) - self.getHeight(node.leftChild))

    def getHeight(self, node):
        try:
            if node == None:
                return -1
            else:
                return 1 + max(self.getHeight(node.leftChild), self.getHeight(node.rightChild))
        except Exception as e:
            logging.info(e)

    def rotateLeftRight(self, node):
        logging.info("Rotating left right...")
        node.leftChild = self.rotateLeft(node.leftChild)
        return self.rotateRight(node)

    def rotateRightLeft(self, node):
        logging.info("Rotating right left...")
        node.rightChild = self.rotateRight(node.rightChild)
        return self.rotateLeft(node)

    def rotateLeft(self, node):
        logging.info("Rotating left")
        b = node.rightChild
        b.parentNode = node.parentNode

        node.rightChild = b.leftChild

        if node.rightChild is not None:
            node.rightChild.parentNode = node

        b.leftChild = node
        node.parentNode = b

        if b.parentNode is not None:
            if b.parentNode.rightChild == node:
                b.parentNode.rightChild = b
            else:
                b.parentNode.leftChild = b

        self.setBalance(node)
        self.setBalance(b)

        return b

    def rotateRight(self, node):
        logging.info("Rotating right")
        b = node.leftChild
        b.parentNode = node.parentNode

        node.leftChild = b.rightChild

        if node.leftChild is not None:
            node.leftChild.parentNode = node

        b.rightChild = node
        node.parentNode = b

        if b.parentNode is not None:
            if b.parentNode.rightChild == node:
                b.parentNode.rightChild = b
            else:
                b.parentNode.leftChild = b

        self.setBalance(node)
        self.setBalance(b)

        return b
