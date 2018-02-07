class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.data > data:
            if not self.leftChild:
                self.leftChild = Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild = Node(data)
            else:
                self.rightChild.insert(data)

    def remove(self, data, parentNode):
        if self.data > data:
            if self.leftChild is not None:
                self.leftChild.remove(data, self)
        elif self.data < data:
            if self.rightChild is not None:
                self.rightChild.remove(data, self)
        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.getMinimum()
                self.rightChild.remove(self.data, self)

            elif parentNode.leftChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild
                parentNode.leftChild = tempNode

            elif parentNode.rightChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild
                parentNode.rightChild = tempNode

    def getMinimum(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.getMinimum()

    def getMaximum(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMaximum()

    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()

        print(self.data)

        if self.rightChild is not None:
            self.rightChild.traverseInOrder()
