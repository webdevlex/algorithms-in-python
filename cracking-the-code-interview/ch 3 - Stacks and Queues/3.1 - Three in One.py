# Three in One: Describe how you could use a single array to implement
# three stacks.


class FixedMultiStack:
    def __init__(self, capacity):
        self.numOfStacks = 3
        self.stackCapacity = capacity
        self.values = [0] * (capacity * self.numOfStacks)
        self.sizes = [0] * self.numOfStacks

    def push(self, stackNum, newItem):
        if self.isFull(stackNum):
            raise ValueError(f"{stackNum} is full")
        else:
            idx = self.getNextIdx(stackNum)
            self.values[idx] = newItem
            self.sizes[stackNum - 1] += 1

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise ValueError(f"{stackNum} is empty")
        else:
            idx = self.getTopIdx(stackNum)
            temp = self.values[idx]
            self.values[idx] = 0
            self.sizes[stackNum - 1] -= 1
            return temp

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise ValueError(f"{stackNum} is empty")
        else:
            idx = self.getTopIdx(stackNum)
            return self.values[idx]

    def isEmpty(self, stackNum):
        return self.sizes[stackNum - 1] <= 0

    def isFull(self, stackNum):
        return self.sizes[stackNum - 1] >= self.stackCapacity

    def getTopIdx(self, stackNum):
        return ((self.sizes[stackNum - 1] - 1) * self.numOfStacks) + (stackNum - 1)

    def getNextIdx(self, stackNum):
        return (self.sizes[stackNum - 1] * self.numOfStacks) + (stackNum - 1)

    def print(self):
        print("values: ", self.values)
        print("sizes: ", self.sizes)
        print()


myStack = FixedMultiStack(2)
myStack.push(1, 1)
myStack.push(1, 1)
myStack.push(2, 2)
myStack.push(2, 2)
myStack.push(3, 3)
myStack.push(3, 3)
myStack.print()
