from Node import Node


class Tree:
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        if not self.rootNode:
            self.rootNode = Node(data)
        else:
            self.rootNode.insert(data)

    def remove(self, data):
        if self.rootNode:
            if self.rootNode.data == data:
                tempNode = Node(None)
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(data, tempNode)
            else:
                self.rootNode.remove(data, None)

    def getMinimum(self):
        if self.rootNode:
            return self.getMinimum

    def getMaximum(self):
        if self.rootNode:
            return self.rootNode.getMaximum()

    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()
