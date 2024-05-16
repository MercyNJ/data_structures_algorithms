#!/usr/bin/env python3
"""
Module contains implementation for:
225. Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""
class MyStack:
    """
    Stack implementation using two queues.
    """
    def __init__(self):
        """
        Initialization.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """ Add elememt to stack."""
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """Removes and returns top element"""
        return self.queue1.pop(0)

    def top(self) -> int:
        """Returns top elem without removing it."""
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1

def test_my_stack():
    stack = MyStack()

    stack.push(1)
    stack.push(2)

    assert stack.top() == 2

    assert stack.pop() == 2

    assert not stack.empty()

    assert stack.pop() == 1

    assert stack.empty()

    print("All test cases passed!")

test_my_stack()
