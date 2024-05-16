#!/usr/bin/env python3
"""
Module contains implementation for:
Queue basic implementations
"""
class Queue:
    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]

    def rear(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[-1]

    def is_full(self):
        if self.max_size is None:
            return False
        return len(self.items) == self.max_size

    def is_empty(self):
        return len(self.items) == 0

# Example usage:
q = Queue(max_size=5)

print("Is the queue empty?", q.is_empty())  # Output: True

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Front element:", q.peek())  # Output: 1
print("Rear element:", q.rear())    # Output: 3

print("Is the queue full?", q.is_full())  # Output: False

print("Dequeue:", q.dequeue())   # Output: 1
print("Dequeue:", q.dequeue())   # Output: 2

print("Is the queue empty?", q.is_empty())  # Output: False

