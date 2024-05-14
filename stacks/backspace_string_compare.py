#!/usr/bin/env python3
"""
Module contains implementation for:
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
"""
from typing import List

# My Implementation
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result_s = []
        if s:
            for c in s:
                if c != '#':
                    result_s.append(c)
                else:
                    if result_s:
                        result_s.pop()

        result_t = []
        if t:
            for ch in t:
                if ch != '#':
                    result_t.append(ch)
                else:
                    if result_t:
                        result_t.pop()
        return result_s == result_t

# can be shortened as
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string: str) -> List[str]:
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return result

        result_s = process_string(s)
        result_t = process_string(t)
        return result_s == result_t

def test_backspaceCompare():
    solution = Solution()
    
    s1, t1 = "ab#c", "ad#c"
    assert solution.backspaceCompare(s1, t1) == True
    
    s2, t2 = "ab##", "c#d#"
    assert solution.backspaceCompare(s2, t2) == True
    
    s3, t3 = "a#c", "b"
    assert solution.backspaceCompare(s3, t3) == False
    
    print("All test cases passed!")

test_backspaceCompare()
