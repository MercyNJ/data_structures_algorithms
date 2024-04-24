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

"""
171. Excel Sheet Column Number
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1

Example 2:

Input: columnTitle = "AB"
Output: 28

Example 3:

Input: columnTitle = "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        # Iterate through the characters of the string in reverse order
        for i in range(len(columnTitle) - 1, -1, -1):
            # Calculate the value of the current character based on its position in the alphabet
            char_value = ord(columnTitle[i]) - ord('A') + 1
            # Multiply the character value by 26 raised to the power of its position
            result += char_value * (26 ** (len(columnTitle) - 1 - i))
        return result

solution = Solution()
print(solution.titleToNumber("A"))  # Output: 1
print(solution.titleToNumber("B"))  # Output: 2
print(solution.titleToNumber("C"))  # Output: 3
print(solution.titleToNumber("Z"))  # Output: 26
print(solution.titleToNumber("AA"))  # Output: 27
print(solution.titleToNumber("AB"))
