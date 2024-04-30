#!/usr/bin/env python3
"""
Module contains implementation for:
459. Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n // 2 + 1):
            if n % length == 0:
                substring = s[:length]
                if substring * (n // length) == s:
                    return True
        return False

def test_repeatedSubstringPattern():
    solution = Solution()

    s1 = "abab"
    expected_output1 = True
    assert solution.repeatedSubstringPattern(s1) == expected_output1, f"Test case 1 failed: Expected {expected_output1}, but got {solution.repeatedSubstringPattern(s1)}"

    s2 = "aba"
    expected_output2 = False
    assert solution.repeatedSubstringPattern(s2) == expected_output2, f"Test case 2 failed: Expected {expected_output2}, but got {solution.repeatedSubstringPattern(s2)}"

    s3 = "abcabcabcabc"
    expected_output3 = True
    assert solution.repeatedSubstringPattern(s3) == expected_output3, f"Test case 3 failed: Expected {expected_output3}, but got {solution.repeatedSubstringPattern(s3)}"

    print("All test cases passed!")

test_repeatedSubstringPattern()
