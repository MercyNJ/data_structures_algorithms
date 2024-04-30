#!/usr/bin/env python3
"""
Module contains implementation for:
434. Number of Segments in a String
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.
Example 1:
Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:
Input: s = "Hello"
Output: 1
"""
class Solution:
    def countSegments(self, s: str) -> int:
        words_s = s.split()
        count = len(words_s)
        return count

#Alternative Implementation
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        in_segment = False

        for char in s:
            # If character is a non-space character and we're not already inside a segment
            if char != ' ' and not in_segment:
                # Increment segment count and set flag to True to indicat inside a segment
                count += 1
                in_segment = True
            # If the current character is a space and we're inside a segment
            elif char == ' ' and in_segment:
                # Reset the flag to False to indicate we're outside a segment
                in_segment = False

        return count

# Example usage:
solution = Solution()
s = "Hello, my name is John"
print(solution.countSegments(s))  # Output: 5
