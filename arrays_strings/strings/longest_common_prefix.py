#!/usr/bin/env python3
"""
Module contains implementation for:

14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
#my implementation

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return result
            
        first_str = strs[0]
        for i in range(len(first_str)):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or first_str[i] != strs[j][i]:
                    return result
            result += first_str[i]
        return result

def test_longest_common_prefix():
    sol = Solution()
    
    strs1 = ["flower", "flow", "flight"]
    output1 = sol.longestCommonPrefix(strs1)
    expected1 = "fl"
    assert output1 == expected1, "Test case 1 failed: Expected '{}', but got '{}'".format(expected1, output1)

    strs2 = ["dog", "racecar", "car"]
    output2 = sol.longestCommonPrefix(strs2)
    expected2 = ""
    assert output2 == expected2, "Test case 2 failed: Expected '{}', but got '{}'".format(expected2, output2)

    print("All test cases passed!")

test_longest_common_prefix()


