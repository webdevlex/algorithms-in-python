class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def add(self, item):
        newNode = QueueNode(item)
        if self.front == None:
            self.front = newNode
            self.back = newNode
        else:
            self.back.setNext(newNode)
            self.back = newNode

    def remove(self):
        if self.front != None:
            if self.front == self.back:
                self.back = None
            self.front = self.front.getNext()
        else:
            raise ValueError("You tried to remove an item from an empty queue")

    def peek(self):
        return self.front

    def isEmpty(self):
        return self.front == None

    def print(self):
        current = self.front
        while current != None:
            print(f"({current.getValue()})", end="")
            if current.getNext() != None:
                print(" -> ", end="")
            current = current.getNext()


class QueueNode:
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
