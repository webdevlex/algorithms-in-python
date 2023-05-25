from LinkedList import LinkedList
from LinkedList import Node


def deleteMiddleNode(node):
    if node == None or node.getNext() == None:
        return False
    node.setValue(node.getNext().getValue())
    node.setNext(node.getNext().getNext())
    return True


myList = LinkedList()
node = Node(5)

myList.insert(0)
myList.insertNode(node)
myList.insert(10)
myList.insert(15)
myList.insert(20)

print("\nBefore: ", end="")
myList.print()

print("After: ", end="")
deleteMiddleNode(node)
myList.print()
