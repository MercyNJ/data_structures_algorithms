#!/usr/bin/env python3
"""
Module contains implementation for:
    67. Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
# 1st approach : Convert binary strings to int then back to binary after addition

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = bin(int(a, 2) + int(b, 2))[2:]
        return result

#2nd Approach
def addBinary(a: str, b: str) -> str:
    result = ""
    carry = 0

    # Iterate over the binary strings from right to left
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
        # Get the current digits from a and b
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Add the digits and the carry
        sum_digits = digit_a + digit_b + carry

        # Calculate the current bit and the carry
        current_bit = sum_digits % 2
        carry = sum_digits // 2

        # Prepend the current bit to the result string
        result = str(current_bit) + result

        # Move to the next digits in a and b
        i -= 1
        j -= 1

    return result

# Test cases
print(addBinary("11", "1"))      # Output: "100"
print(addBinary("1010", "1011")) # Output: "10101"
