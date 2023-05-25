from LinkedList import LinkedList


def removeDups(linkedList):
    myMap = {}
    previous = None
    current = linkedList.getHead()
    while current != None:
        currentValue = current.getValue()
        if currentValue in myMap:
            previous.setNext(current.getNext())
        else:
            myMap[currentValue] = True
            previous = current
        current = current.getNext()


def removeDups2(linkedList):
    current = linkedList.getHead()
    while current != None:
        runner = current
        while runner != None:
            if (
                runner.getNext() != None
                and runner.getNext().getValue() == current.getValue()
            ):
                runner.setNext(runner.getNext().getNext())
            else:
                runner = runner.getNext()
        current = current.getNext()


myList = LinkedList()

myList.insert(0)
myList.insert(5)
myList.insert(10)
myList.insert(15)
myList.insert(20)
myList.insert(0)
myList.insert(5)
myList.insert(10)
myList.insert(15)
myList.insert(20)

print("\nBefore: ", end="")
myList.print()

print("After: ", end="")
removeDups2(myList)
myList.print()
