#!/usr/bin/env python3
"""
Module contains implementation for:
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
from typing import Optional

# Implementation only returns True Or False Bsed on absence/presnce of cycle
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


# Implementation returns where loops start or None
def find_loop(self):
    """
    Finds loop in a single linked list
    Return None if no loop , if found where loop starts.
    """
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            #reset slow only- if fast catches up and they meet means we have a loop
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

#geeksforgeeks implementation
class Node:

    # Constructor to initialize node
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # insert node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print linkedlist
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):

            # if node already in set then its repeated.
            if (temp in s):
                return True

            # if seeing node the first time, insert it in hash
            s.add(temp)

            temp = temp.next

        return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if(llist.detectLoop()):
    print("Loop Found")
else:
    print("No Loop ")
