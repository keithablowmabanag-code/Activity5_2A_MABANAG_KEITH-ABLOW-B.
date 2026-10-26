class ArrayStack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack overflow: the stack is full.")
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow: cannot peek at an empty stack.")
        return self.items[-1]

    def display(self):
        return self.items.copy()