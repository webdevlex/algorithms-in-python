from LinkedList import LinkedList


def returnKthToLast(linkedList, k):
    current = linkedList.getHead()
    kthElement = linkedList.getCount() - k
    for i in range(kthElement):
        current = current.getNext()

    print(f"Kth element is {current.getValue()}")


def returnKthToLast2(node, k):
    if node == None:
        return 0

    currentK = returnKthToLast(node.getNext(), k) + 1
    if currentK == k:
        print(f"Kth element is {node.getValue()}")

    return currentK


myList = LinkedList()
myList.insert(0)
myList.insert(5)
myList.insert(10)
myList.insert(15)
myList.insert(20)

print("\nBefore: ", end="")
myList.print()

print("After: ", end="")
returnKthToLast(myList)
myList.print()
