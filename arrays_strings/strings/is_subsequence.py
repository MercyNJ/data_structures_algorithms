#!/usr/bin/env python3
"""
Module contains implementation for:
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""
#1st Implementation
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        list_t = [char for char in t]
        idx_s = 0

        for char_t in list_t:
            if idx_s < len(s) and s[idx_s] == char_t:
                idx_s += 1
        return idx_s == len(s)

def test_is_subsequence():
    solution = Solution()
    
    s1 = "abc"
    t1 = "ahbgdc"
    assert solution.isSubsequence(s1, t1) == True, "Test case 1 failed"
    
    s2 = "axc"
    t2 = "ahbgdc"
    assert solution.isSubsequence(s2, t2) == False, "Test case 2 failed"
    
    print("All test cases passed!")

test_is_subsequence()

#2nd Implementation: Iterate over both strings at once
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
