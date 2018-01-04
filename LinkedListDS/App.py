from LinkedList import LinkedList
import sys

print(sys.version)
print("\n")

linkedList = LinkedList()

linkedList.insertEnd(1)
linkedList.insertEnd(2)
linkedList.insertStart(4)
linkedList.insertStart(4)

linkedList.traverseList()
print("\nSize: " + str(linkedList.counter) + "\n")

print("-------------------------")

# Removes 1 in the linked List
linkedList.remove(4)
linkedList.remove(1)
linkedList.traverseList()
print("\nSize: " + str(linkedList.counter) + "\n")
