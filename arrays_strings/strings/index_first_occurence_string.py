#!/usr/bin/env python3
"""
Module contains implementation for:
    28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

#my implementation
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """ Find index of first occurence of a string."""
        n = len(needle)

        if needle not in haystack or n == 0:
            return -1
        else:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i: i + n] == needle:
                        return i

def test_strStr():
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("mississippi", "issip", 4)
    ]
    
    solution = Solution()
    for haystack, needle, expected_output in test_cases:
        result = solution.strStr(haystack, needle)
        assert result == expected_output, "For haystack '{}', needle '{}', expected {}, but got {}".format(haystack, needle, expected_output, result)
    print("All test cases passed!")

test_strStr()

