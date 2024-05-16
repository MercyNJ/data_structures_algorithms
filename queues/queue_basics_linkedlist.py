#!/usr/bin/env python3
"""
Module contains implementation for:
Queue basic implementations using linked lists
"""

class Node:
    def __init__(self, data):
        """Initialize a node with data and a reference to the next node."""
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.front = None
        self.rear = None

    def enqueue(self, item):
        """Add an element to the rear of the queue."""
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        return data

    def peek(self):
        """Get the element at the front of the queue without removing it."""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data

    def rear_element(self):
        """Get the element at the rear of the queue without removing it."""
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.rear.data

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

# Example usage:
q = Queue()

print("Is the queue empty?", q.is_empty())  # Output: True

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Front element:", q.peek())  # Output: 1
print("Rear element:", q.rear_element())    # Output: 3

print("Dequeue:", q.dequeue())   # Output: 1
print("Dequeue:", q.dequeue())   # Output: 2

print("Is the queue empty?", q.is_empty())  # Output: False
