# stack ds

class Stack:
    def __init__(self, vals):
        self.stack = vals
        print(len(self.stack) == 0)

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# making a stack without built-ins


class ManualStack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def push(self, value):
        if self.top + value >= self.capacity:
            return -1
            print("stack overflow")
        self.stack