# Return Kth to Last: Implement an algorithm to find the kth to last element
# of a singly linked list.

from LinkedList import LinkedList


# Solution 1: If we know the length of the linked list
def returnKthToLast1(head, k, listLength):
    current = head
    kthElement = listLength - k
    for i in range(kthElement):
        current = current.getNext()

    print(f"Kth element is {current.getValue()}")


# Solution 2: Using recurssion
def returnKthToLast2(node, k):
    if node == None:
        return 0

    currentK = returnKthToLast2(node.getNext(), k) + 1
    if currentK == k:
        print(f"Kth element is {node.getValue()}")

    return currentK


# Solution 3: Using two pointers
def returnKthToLast3(node, k):
    left = node
    right = node

    for i in range(k):
        if not right:
            return None
        right = right.getNext()

    while right:
        left = left.getNext()
        right = right.getNext()

    return left


myList = LinkedList()
myList.insert(0)
myList.insert(5)
myList.insert(10)
myList.insert(15)
myList.insert(20)

returnKthToLast1(myList.getHead(), 3, 5)

returnKthToLast2(myList.getHead(), 3)

kthElement = returnKthToLast3(myList.getHead(), 3)
print(f"Kth element is {kthElement.getValue()}")
