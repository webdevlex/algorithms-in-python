class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        self.top = StackNode(item, self.top)
        self.size += 1

    def pop(self):
        if self.top == None:
            raise ValueError("You tried to pop from an empty stack")
        value = self.top.getValue()
        self.top = self.top.getNext()
        self.size -= 1
        return value

    def peek(self):
        return self.top.getValue()

    def isEmpty(self):
        return self.top == None

    def getSize(self):
        return self.size

    def print(self):
        current = self.top
        while current != None:
            print(f"({current.getValue()})", end="")
            if current.getNext() != None:
                print(" -> ", end="")
            current = current.getNext()


class StackNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def getValue(self):
        return self.data

    def setValue(self, data):
        self.data = data
