from LinkedList import LinkedList
from LinkedList import Node


def partition(linkedList, x):
    head = linkedList.getHead()
    h1 = l1 = Node(0)
    h2 = l2 = Node(0)
    while head:
        if head.getValue() < x:
            l1.setNext(head)
            l1 = l1.getNext()
        else:
            l2.setNext(head)
            l2 = l2.getNext()
        head = head.getNext()
    l2.setNext(None)
    l1.setNext(h2.getNext())
    return h1.getNext()


myList = LinkedList()
myList.insert(3)
myList.insert(5)
myList.insert(8)
myList.insert(5)
myList.insert(10)
myList.insert(2)
myList.insert(1)

print("\nBefore: ", end="")
myList.print()

print("After: ", end="")
partition(myList, 5)
myList.print()
