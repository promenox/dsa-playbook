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
        # list items are the same fixed size and given by cap
        self.stack = [None] * capacity
        self.capacity = capacity
        self.top = -1
        # Notes: try an arb bytes workflow in C

    def isEmpty(self):
        return self.top == -1

    def push(self, value):
        # check avalible space
        if self.capacity <= self.top:
            raise OverflowError("Stack is Full")
        # store value and increment pointer
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop on Empty Stack")
        val = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return val

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek on Empty Stack")
        return self.stack[self.top]

    def size(self):
        return self.top + 1
