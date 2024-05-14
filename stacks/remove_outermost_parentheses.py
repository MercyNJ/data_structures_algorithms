#!/usr/bin/env python3
"""
Module contains implementation for:
1021. Remove Outermost Parentheses
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
    For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.
Example 1:
Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        stack = []

        primitive_start = 0  # start index of a primitive string

        for i, char in enumerate(s):
            if char == '(':
                stack.append(char)  # Push opening parenthesis onto the stack
            else:
                stack.pop()  # Pop an opening parenthesis from the stack

                # If the stack becomes empty after popping, it means we've identified a primitive string
                if not stack:
                    # Extract the primitive string (excluding outermost parentheses) and add it to the result
                    result += s[primitive_start+1:i]
                    primitive_start = i + 1  # Update the start index for the next primitive string

        return result
