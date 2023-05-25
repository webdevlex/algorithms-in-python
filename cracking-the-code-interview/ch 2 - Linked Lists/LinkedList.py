class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def getHead(self):
        return self.head

    def setHead(self, value):
        self.head = Node(value)

    def setHeadNode(self, node):
        self.head = node

    def insert(self, value):
        current = self.head

        if current == None:
            self.head = Node(value)
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(value))

        self.count += 1

    def insertNode(self, node):
        current = self.head

        if current == None:
            self.head = node
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(node)
            self.count += 1

    def remove(self, key):
        current = self.head

        if current != None:
            if current.getValue() == key:
                self.head = current.getNext()
            else:
                runner = current.getNext()
                while runner != None and runner.getValue() != key:
                    current = runner
                    runner = runner.getNext()

                if runner != None:
                    current.setNet(runner.getNext())
        self.count -= 1

    def print(self):
        current = self.head
        while current != None:
            print(f"({current.getValue()})", end="")
            if current.getNext() != None:
                print(" -> ", end="")
            current = current.getNext()
        print()
