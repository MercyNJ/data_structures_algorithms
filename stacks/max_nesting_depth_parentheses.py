#!/usr/bin/env python3
"""
Module contains implementation for:
1614. Maximum Nesting Depth of the Parentheses
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.
"""
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
                # ensures we return max encountered , not simply len of stack
                # even if closing parentheses are balanced out
                max_depth = max(max_depth, len(stack))
            elif char == ")":
                stack.pop()
        return max_depth

def test_solution():
    solution = Solution()

    s1 = "(1+(2*3)+((8)/4))+1"
    assert solution.maxDepth(s1) == 3

    s2 = "(1)+((2))+(((3)))"
    assert solution.maxDepth(s2) == 3

    s3 = "()(())((()()))"
    assert solution.maxDepth(s3) == 3

    print("All test cases passed!")

test_solution()
