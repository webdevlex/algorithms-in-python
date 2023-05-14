class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    # ----------------------------------
    # Push
    # ----------------------------------
    def push(self, value):
        if self.size + 1 == len(self.stack):
            raise Exception("Stack is full.")
        self.stack.append(value)
        self.size += 1

    # ----------------------------------
    # Pop
    # ----------------------------------
    def pop(self):
        if self.size <= 0:
            raise Exception("Stack is empty.")
        top_of_stack = self.stack.pop()
        self.size -= 1
        return top_of_stack

    # ----------------------------------
    # Print
    # ----------------------------------
    def print(self):
        print(self.stack)
