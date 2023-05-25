from LinkedList import LinkedList
from LinkedList import Node


def intersection(l1, l2):
    nodes = {}
    while l1:
        nodes[l1] = True
        l1 = l1.getNext()

    while l2:
        if l2 in nodes:
            return l2
        l2 = l2.getNext()

    return None


node = Node(3)

myList1 = LinkedList()
myList1.insert(0)
myList1.insert(1)
myList1.insert(2)
myList1.insertNode(node)
myList1.insert(4)
myList1.insert(5)

myList2 = LinkedList()
myList2.insert(0)
myList2.insert(1)
myList2.insert(2)
myList2.insertNode(node)
myList2.insert(4)
myList2.insert(5)

output = intersection(myList1.getHead(), myList2.getHead())
print(output)
