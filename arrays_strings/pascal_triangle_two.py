"""
Leetcode 119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it
Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Generate a single row of pascal triangle.
        """
        row = []
        cols = rowIndex + 1

        for j in range(cols):
            if j == 0 or j == rowIndex:
                row.append(1)
            else:
                value = row[-1] * (rowIndex - j + 1) // j
                row.append(value)
        return row

def test_getRow():
    solution = Solution()
    
    expected_output_1 = [1, 3, 3, 1]
    output_1 = solution.getRow(3)
    assert output_1 == expected_output_1, "Test case 1 failed: Expected {}, but got {}".format(expected_output_1, output_1)
    
    expected_output_2 = [1]
    output_2 = solution.getRow(0)
    assert output_2 == expected_output_2, "Test case 2 failed: Expected {}, but got {}".format(expected_output_2, output_2)
    
    expected_output_3 = [1, 1]
    output_3 = solution.getRow(1)
    assert output_3 == expected_output_3, "Test case 3 failed: Expected {}, but got {}".format(expected_output_3, output_3)
    
    print("All test cases passed!")

test_getRow()

