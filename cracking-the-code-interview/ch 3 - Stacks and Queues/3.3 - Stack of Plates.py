from stack import Stack


class StackOfPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [Stack()]
        self.currentStackIdx = 0

    def push(self, value):
        currentStack = self.getCurrentStack()
        if self.stackIsFull(currentStack):
            self.stacks.append(Stack())
            self.currentStackIdx += 1
            currentStack = self.getCurrentStack()
        currentStack.push(value)

    def pop(self):
        currentStack = self.getCurrentStack()
        value = currentStack.pop()
        if currentStack.isEmpty():
            if len(self.stacks) > 1:
                self.stacks.remove(currentStack)
            self.currentStackIdx -= 1 if self.currentStackIdx > 0 else 0
            currentStack = self.getCurrentStack()
        return value

    def peek(self):
        currentStack = self.getCurrentStack()
        return currentStack.peek()

    def getCurrentStack(self):
        return self.stacks[self.currentStackIdx]

    def stackIsFull(self, currentStack):
        return currentStack.getSize() >= self.capacity

    def print(self):
        for stack in self.stacks:
            stack.print()
            print()


myStack = StackOfPlates(2)
myStack.print()
