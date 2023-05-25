from LinkedList import LinkedList
from LinkedList import Node


def sumList(l1, l2):
    head = sumListHelper(l1, l2)
    result = LinkedList()
    result.setHeadNode(head)
    return result


def sumListHelper(l1, l2, carry=0):
    if l1 == None and l2 == None and carry == 0:
        return None

    result = Node()
    sum = carry
    if l1 != None:
        sum += l1.getValue()
    if l2 != None:
        sum += l2.getValue()
    result.setValue(sum % 10)

    nextL1 = None if l1 == None else l1.getNext()
    nextL2 = None if l2 == None else l2.getNext()
    carry = 1 if sum >= 10 else 0

    nextNode = sumListHelper(nextL1, nextL2, carry)
    result.setNext(nextNode)
    return result


myList1 = LinkedList()


myList2 = LinkedList()
myList2.insert(1)
myList2.insert(1)


output = sumList(myList1.getHead(), myList2.getHead())
output.print()

# def getNum(node):
#     if node == None:
#         return ""

#     num = getNum(node.getNext())
#     num += str(node.getValue())
#     return num


# def linkify(numAsStr):
#     current = None
#     for num in numAsStr:
#         newNode = Node(int(num))
#         newNode.setNext(current)
#         current = newNode
#     newList = LinkedList()
#     newList.setHeadNode(current)
#     return newList


# def sumList(list1, list2):
#     num1 = int(getNum(list1.getHead()))
#     num2 = int(getNum(list2.getHead()))
#     sum = num1 + num2
#     return linkify(str(sum))
