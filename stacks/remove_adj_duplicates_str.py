#!/usr/bin/env python3
"""
Module contains implementation for:
1047. Remove All Adjacent Duplicates In String
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:

Input: s = "azxxzy"
Output: "ay"
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        result = ""

        for char in s:
            if not stack or char != stack[-1]:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()

        for char in stack:
            result += char
        return result

def test_remove_duplicates():
    sol = Solution()

    s1_input = "abbaca"
    expected_output1 = "ca"
    result1 = sol.removeDuplicates(s1_input)
    assert result1 == expected_output1, "Test case 1 failed: Expected {}, but got {}".format(expected_output1, result1)

    s2_input = "azxxzy"
    expected_output2 = "ay"
    result2 = sol.removeDuplicates(s2_input)
    assert result2 == expected_output2, "Test case 2 failed: Expected {}, but got {}".format(expected_output2, result2)

    print("All test cases passed!")

test_remove_duplicates()

# use join method
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1]:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()
        return ''.join(stack)
