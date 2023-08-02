# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

from LinkedList import LinkedList


# Solution 1: With temproray buffer
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


# Solution 2: Without temproray buffer
def removeDups2(linkedList):
    current = linkedList.getHead()
    while current != None:
        runner = current
        while runner.getNext() != None:
            if runner.getNext().getValue() == current.getValue():
                runner.setNext(runner.getNext().getNext())
            else:
                runner = runner.getNext()
        current = current.getNext()


myList = LinkedList()

myList.insert(20)
myList.insert(20)
myList.insert(20)

print("\nBefore: ", end="")
myList.print()

print("After: ", end="")
removeDups2(myList)
myList.print()
