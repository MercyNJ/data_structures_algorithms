#!/usr/bin/env python3
"""
Module contains implementation for:
876. Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node
"""
# MY APPROACH
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get count of nodes
        node_count = 0
        current = head
        while current:
            node_count += 1
            current = current.next

        middle_index = node_count // 2

        # Traverse the linked list again to find the middle node
        current = head
        current_index = 0
        while current:
            if current_index == middle_index:
                return current
            current_index += 1
            current = current.next
        return None

# ALTERNATIVE IMPLEMENTATION- 2 pointers
# by end of iteration slow wil be in middle
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

