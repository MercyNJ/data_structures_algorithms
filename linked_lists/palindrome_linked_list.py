#!/usr/bin/env python3
"""
Module contains implementation for:
Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.
"""
from typing import Optional

#1st Approach - Using Stack
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        current = head
        while current:
            stack.append(current.val)
            current = current.next

        current = head
        while current:
            node = stack.pop()
            if node != current.val:
                return False
            current = current.next
        return True

def test_is_palindrome():
    # Test case 1: Palindrome list
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    two_dup = ListNode(2)
    one_dup = ListNode(1)

    one.next = two
    two.next = three
    three.next = two_dup
    two_dup.next = one_dup

    solution = Solution()
    assert solution.isPalindrome(one) == True

    # Test case 2: Non-palindrome list
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    assert solution.isPalindrome(one) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_palindrome()

#2nd Approach - Reversing the linked list
"""
    Finding the middle of the linked list.
    Reversing the second half.
    Comparing the first and reversed second halves for palindrome check.
    Reconstructing the original linked list by reversing the second half and
    attaching it back to the first half.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Find the middle of the linked list(slow)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Step 3: Check if the first half and second half are identical
        second_half = prev
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True

def test_is_palindrome():
    # Test case 1: Palindrome list
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    two_dup = ListNode(2)
    one_dup = ListNode(1)

    one.next = two
    two.next = three
    three.next = two_dup
    two_dup.next = one_dup

    solution = Solution()
    assert solution.isPalindrome(one) == True

    # Test case 2: Non-palindrome list
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    assert solution.isPalindrome(one) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_is_palindrome()
