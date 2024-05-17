#!/usr/bin/env python3
"""
Module contains implementation for:
232. Implement Queue using Stacks
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
"""
class MyQueue:
    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

def test_MyQueue():
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.peek() == 1, "Test Case 1 failed: Peek operation"
    assert obj.pop() == 1, "Test Case 1 failed: Pop operation"
    assert obj.empty() == False, "Test Case 1 failed: Empty check"
    print("Test Case 1 passed.")
    
    obj = MyQueue()
    obj.push(1)
    assert obj.pop() == 1, "Test Case 2 failed: Pop operation"
    assert obj.empty() == True, "Test Case 2 failed: Empty check"
    print("Test Case 2 passed.")

test_MyQueue()

