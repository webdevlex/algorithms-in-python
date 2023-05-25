from stack import Stack
from stack import StackNode


# Solution 1
class StackNodeWithMin(StackNode):
    def __init__(self, data=None, min=None, next=None):
        self.data = data
        self.next = next
        self.min = min

    def setMin(self, value):
        self.min = value

    def getMin(self):
        return self.min


class StackWithMin(Stack):
    def push(self, item):
        if self.top == None or item < self.top.getMin():
            self.top = StackNodeWithMin(item, item, self.top)
        else:
            self.top = StackNodeWithMin(item, self.top.getMin(), self.top)

    def getMin(self):
        return self.top.getMin()


# Solution 2
class StackWithMin2(Stack):
    def __init__(self):
        self.top = None
        self.minsTop = None

    def push(self, value):
        if self.top == None or value <= self.minsTop.getValue():
            self.minsTop = StackNode(value, self.minsTop)
        super().push(value)

    def pop(self):
        value = super().pop()
        if value == self.minsTop.getValue():
            self.minsTop = self.minsTop.getNext()
        return value

    def getMin(self):
        if self.minsTop == None:
            raise ValueError("You tried to get the min from an empty stack")
        return self.minsTop.getValue()


myMinStack = StackWithMin2()
print(myMinStack.getMin())
