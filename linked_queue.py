class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot dequeue from an empty queue.")

        item = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue underflow: cannot peek at an empty queue.")
        return self.head.data

    def display(self):
        items = []
        current = self.head

        while current is not None:
            items.append(current.data)
            current = current.next

        return items