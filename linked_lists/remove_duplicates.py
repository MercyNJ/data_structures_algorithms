#!/usr/bin/env python3
"""
Module contains implementation for:
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current:
            while current.next:
                if current.val == current.next.val:
                    current.next = current.next.next
                else:
                    break
            current = current.next
        return head

def test_deleteDuplicates():
    # Test Case 1
    head1 = ListNode(1)
    head1.next = ListNode(1)
    head1.next.next = ListNode(2)

    solution = Solution()
    result1 = solution.deleteDuplicates(head1)

    # Traverse the modified linked list and assert the values of each node
    assert result1.val == 1
    assert result1.next.val == 2
    assert result1.next.next is None

    # Test Case 2
    head2 = ListNode(1)
    head2.next = ListNode(1)
    head2.next.next = ListNode(2)
    head2.next.next.next = ListNode(3)
    head2.next.next.next.next = ListNode(3)

    result2 = solution.deleteDuplicates(head2)

    # Traverse the modified linked list and assert the values of each node
    assert result2.val == 1
    assert result2.next.val == 2
    assert result2.next.next.val == 3
    assert result2.next.next.next is None

    print("All test cases passed!")

test_deleteDuplicates()
