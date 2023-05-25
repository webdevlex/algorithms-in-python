from stack import Stack


def sortStack(stack):
    tempStack = Stack()
    while not stack.isEmpty():
        tempValue = stack.pop()
        while not tempStack.isEmpty() and tempValue <= tempStack.peek():
            stack.push(tempStack.pop())
        tempStack.push(tempValue)

    while not tempStack.isEmpty():
        stack.push(tempStack.pop())


myStack = Stack()
myStack.push(5)
myStack.push(3)
myStack.push(1)
myStack.push(2)
myStack.push(4)
# myStack.print()

sortStack(myStack)
myStack.print()
# myStack.print()
