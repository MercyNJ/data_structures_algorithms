#!/usr/bin/env python3
"""
Module contains implementation for:
415. Add Strings
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        
        # iterate from right to left
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0:
            digit1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            digit2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10

            result = chr(digit + ord('0')) + result

            i -= 1
            j -= 1
        if carry:
            result = '1' + result
        return result

def test_addStrings():
    num1_1 = "11"
    num2_1 = "123"
    expected_output_1 = "134"
    result_1 = Solution().addStrings(num1_1, num2_1)
    assert result_1 == expected_output_1, f"Test case 1 failed: Expected {expected_output_1}, but got {result_1}"

    num1_2 = "456"
    num2_2 = "77"
    expected_output_2 = "533"
    result_2 = Solution().addStrings(num1_2, num2_2)
    assert result_2 == expected_output_2, f"Test case 2 failed: Expected {expected_output_2}, but got {result_2}"

    num1_3 = "0"
    num2_3 = "0"
    expected_output_3 = "0"
    result_3 = Solution().addStrings(num1_3, num2_3)
    assert result_3 == expected_output_3, f"Test case 3 failed: Expected {expected_output_3}, but got {result_3}"

    print("All test cases passed!")

test_addStrings()
