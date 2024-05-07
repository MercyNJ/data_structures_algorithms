#!/usr/bin/env python3
"""
Module contains implementation for:
1290. Convert Binary Number in a Linked List to Integer
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""
# My Approach
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = ""
        current = head
        while current:
            result += str(current.val)
            current = current.next

        decimal = 0
        for i in range(len(result)):
            binary_digit = int(result[i])
            power_two = 2 ** (len(result) - i - 1)
            product = binary_digit * power_two
            decimal += product
        return decimal

# A better Approach
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        current = head

        while current:
            decimal = decimal * 2 + current.val
            current = current.next
        return decimal
