from LinkedList import LinkedList
from LinkedList import Node


def loopDetection(l1):
    nodes = {}
    while l1:
        if l1 in nodes:
            return l1
        nodes[l1] = True
        l1 = l1.getNext()
    return None


myList = LinkedList()
node = Node(3)


myList.insert(0)
myList.insert(1)
myList.insert(2)
myList.insertNode(node)
myList.insert(4)
myList.insert(5)
myList.insertNode(node)

output = loopDetection(myList.getHead())
print(output.getValue())
