class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setItem(self, item):
        self.item = item

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def getHead(self):
        return self.head

    def setHead(self, item):
        self.head = Node(item)

    def setHeadNode(self, node):
        self.head = node

    def insert(self, item):
        current = self.head

        if current == None:
            self.head = Node(item)
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))

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
            if current.getItem() == key:
                self.head = current.getNext()
            else:
                runner = current.getNext()
                while runner != None and runner.getItem() != key:
                    current = runner
                    runner = runner.getNext()

                if runner != None:
                    current.setNet(runner.getNext())

        self.count -= 1

    def dequeue(self):
        current = self.head
        if current == None:
            raise ValueError("you are trying to dequeue from an empty list")
        self.head = self.head.getNext()
        self.count -= 1
        return current

    def getSize(self):
        return self.count

    def print(self):
        current = self.head
        while current != None:
            print(f"({current.getItem()})", end="")
            if current.getNext() != None:
                print(" -> ", end="")
            current = current.getNext()
        print()
