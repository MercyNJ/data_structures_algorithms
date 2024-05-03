#!/usr/bin/env python3
"""
Module contains implementation for:
203. Remove Linked List Elements
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        while current:
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return dummy.next

def test_remove_elements():
    sol = Solution()
    
    # Test Case 1
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(6)
    head1.next.next.next = ListNode(3)
    head1.next.next.next.next = ListNode(4)
    head1.next.next.next.next.next = ListNode(5)
    head1.next.next.next.next.next.next = ListNode(6)
    val1 = 6
    expected_output1 = [1, 2, 3, 4, 5]
    output1 = sol.removeElements(head1, val1)
    assert [node.val for node in output1] == expected_output1, "Test Case 1 Failed"
    
    # Test Case 2
    head2 = None
    val2 = 1
    expected_output2 = []
    output2 = sol.removeElements(head2, val2)
    assert output2 == expected_output2, "Test Case 2 Failed"
    
    # Test Case 3
    head3 = ListNode(7)
    head3.next = ListNode(7)
    head3.next.next = ListNode(7)
    head3.next.next.next = ListNode(7)
    val3 = 7
    expected_output3 = []
    output3 = sol.removeElements(head3, val3)
    assert output3 == expected_output3, "Test Case 3 Failed"

    print("All test cases passed.")

test_remove_elements()
