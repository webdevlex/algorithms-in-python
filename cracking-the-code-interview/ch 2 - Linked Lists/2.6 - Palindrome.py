from LinkedList import LinkedList
from LinkedList import Node


def palindrome(node):
    copier = node
    newNode = None
    while copier:
        copy = Node(copier.getValue())
        copy.setNext(newNode)
        newNode = copy
        copier = copier.getNext()

    while node and newNode:
        if node.getValue() != newNode.getValue():
            return False
        node = node.getNext()
        newNode = newNode.getNext()

    return node == None and newNode == None


myList = LinkedList()

myList.insert("a")
myList.insert("a")
myList.insert("b")
myList.insert("b")
myList.insert("a")
myList.insert("a")
myList.insert("a")
# myList.insert(15)
# myList.insert(20)

output = palindrome(myList.getHead())
print(output)
