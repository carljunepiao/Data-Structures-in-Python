import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class Node():
    def __init__(self, data, parentNode):
        self.data = data
        self.parentNode = parentNode
        self.rightChild = None
        self.leftChild = None
        self.balance = 0

    def insert(self, data, parentNode):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = Node(data, parentNode)
            else:
                self.leftChild.insert(data, parentNode)
        else:
            if not self.rightChild:
                self.rightChild = Node(data, parentNode)
            else:
                self.rightChild.insert(data, parentNode)

        return parentNode

    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()

        if self.rightChild:
            self.rightChild.traverseInOrder()

        logging.info(self.data)

    def getMax(self):
        if not self.rightChild:
            return self.data
        else:
            return self.rightChild.getMax()

    def getMin(self):
        if not self.leftChild:
            return self.data
        else:
            return self.leftChild.getMin()
