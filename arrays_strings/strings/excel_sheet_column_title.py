#!/usr/bin/env python3
"""
Module contains implementation for:
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            # Subtract 1 to handle 1-based indexing
            columnNumber -= 1
            # Convert the current digit to a character and prepend it to the title
            title = chr(columnNumber % 26 + ord('A')) + title
            # Update columnNumber to consider the next digit
            columnNumber //= 26
        return title
def test_excel_column_title():
    solution = Solution()  # Create an instance of the Solution class
    test_cases = [
        (1, "A"),
        (28, "AB"),
        (701, "ZY")
    ]

    for columnNumber, expected_output in test_cases:
        output = solution.convertToTitle(columnNumber)  # Call the method on the instance
        assert output == expected_output, f"For columnNumber = {columnNumber}, expected {expected_output}, but got {output}"

    print("All test cases passed!")

test_excel_column_title()
