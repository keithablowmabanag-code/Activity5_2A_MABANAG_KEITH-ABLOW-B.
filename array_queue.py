class ArrayQueue:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Queue capacity must be greater than zero.")

        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue overflow: the queue is full.")

        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")

        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot peek at an empty queue.")
        return self.items[self.front]

    def display(self):
        items = []

        for i in range(self.size):
            index = (self.front + i) % self.capacity
            items.append(self.items[index])

        return items