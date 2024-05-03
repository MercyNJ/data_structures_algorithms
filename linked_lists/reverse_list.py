#!/usr/bin/env python3
"""
Module contains implementation for:
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


# Recursive approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverseUtil(self, curr, prev):

        # If last node mark it head
        if curr.next is None:
            self.head = curr

            curr.next = prev
            return

        # Save curr.next node for recursive call
        next = curr.next

        # And update next
        curr.next = prev

        self.reverseUtil(next, curr)

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data, end=" ")
            temp = temp.next


# Driver code
llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("Given linked list")
llist.printList()

llist.reverse()

print ("\nReversed linked list")
llist.printList()
