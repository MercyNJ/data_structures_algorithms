#!/usr/bin/env python3
"""
Module contains implementation for:
21. Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next


def test_mergeTwoLists():
    solution = Solution()

    # Test Case 1
    list1_1 = ListNode(1)
    list1_2 = ListNode(2)
    list1_3 = ListNode(4)
    list1_1.next = list1_2
    list1_2.next = list1_3

    list2_1 = ListNode(1)
    list2_2 = ListNode(3)
    list2_3 = ListNode(4)
    list2_1.next = list2_2
    list2_2.next = list2_3

    merged_result_1 = solution.mergeTwoLists(list1_1, list2_1)
    assert merged_result_1.val == 1
    assert merged_result_1.next.val == 1
    assert merged_result_1.next.next.val == 2
    assert merged_result_1.next.next.next.val == 3
    assert merged_result_1.next.next.next.next.val == 4
    assert merged_result_1.next.next.next.next.next.val == 4
    assert merged_result_1.next.next.next.next.next.next is None

    # Test Case 2
    merged_result_2 = solution.mergeTwoLists(None, None)
    assert merged_result_2 is None

    # Test Case 3
    list1_empty = None
    list2_0 = ListNode(0)

    merged_result_3 = solution.mergeTwoLists(list1_empty, list2_0)
    assert merged_result_3.val == 0
    assert merged_result_3.next is None

    print("All test cases passed!")

test_mergeTwoLists()
