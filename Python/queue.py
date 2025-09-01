class Queue:
    def __init__(self, vals):
        self.queue = vals

    def isEmpty(self):
        return(len(self.queue) == 0)

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        return self.queue.remove(0)

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
            return -1
        return self.queue[0]

    def size(self):
        return len(self.queue)
