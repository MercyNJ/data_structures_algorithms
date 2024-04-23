#!/usr/bin/env python3
"""
Module contains implementation for:
    20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

LOGIC:
    Initialize an empty stack.
    Traverse the input string character by character.
    If the current character is an opening bracket (i.e., '(', '{', '['), push it onto the stack.

    If the current character is a closing bracket (i.e., ')', '}', ']'), check if the stack is empty. If it is empty, return false, because the closing bracket does not have a corresponding opening bracket. Otherwise, pop the top element from the stack and check if it matches the current closing bracket. If it does not match, return false, because the brackets are not valid.

    After traversing the entire input string, if the stack is empty, return true, because all opening brackets have been matched with their corresponding closing brackets. Otherwise, return false, because some opening brackets have not been matched with their corresponding closing brackets.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """ Check if given string is valid. """
        stack = []
        # Opening brackets are keys, closing -values
        brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            # if its an opening bracket, push it onto stack
            if char in brackets:
                stack.append(char)
            # if its a closing bracket
            elif char in brackets.values():
                # if stack is empty or last opening bracket doesnt match
                if not stack or brackets[stack.pop()] != char:
                    return False
        # If there are any remaining opening brackets on the stack
        if stack:
            return False
        else:
            return True

def test_isValid():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("(", False),
        ("}", False),
        ("}{", False)
    ]
    
    solution = Solution()
    for s, expected_output in test_cases:
        result = solution.isValid(s)
        assert result == expected_output, "For input '{}', expected {}, but got {}".format(s, expected_output, result)
    print("All test cases passed!")

test_isValid()
