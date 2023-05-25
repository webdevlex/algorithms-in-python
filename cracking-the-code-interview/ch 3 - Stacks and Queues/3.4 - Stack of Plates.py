from stack import Stack


class MyQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def add(self, value):
        if not self.outStack.isEmpty():
            self.moveItemsToInStack()
        self.inStack.push(value)

    def remove(self):
        if self.inStack.isEmpty() and self.outStack.isEmpty():
            ValueError("you trying to remove from an empty queue")
        elif self.outStack.isEmpty():
            self.moveItemsToOutStack()
        return self.outStack.pop()

    def peek(self):
        if self.inStack.isEmpty() and self.outStack.isEmpty():
            ValueError("you trying to peek into an empty queue")
        elif self.outStack.isEmpty():
            self.moveItemsToOutStack()
        return self.outStack.peek().getValue()

    def moveItemsToOutStack(self):
        while not self.inStack.isEmpty():
            value = self.inStack.pop()
            self.outStack.push(value)

    def moveItemsToInStack(self):
        while not self.outStack.isEmpty():
            value = self.outStack.pop()
            self.inStack.push(value)

    def isEmpty(self):
        return self.inStack.isEmpty() and self.outStack.isEmpty()


myQueue = MyQueue()
