#!/usr/bin/env python3
"""
Module contains implementation for:
    58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_list = s.split()

        if words_list:
            last_word = words_list[-1]
            return len(last_word)
        else:
            return 0

def test_lengthOfLastWord():
    test_cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6)
    ]
    
    solution = Solution()
    for s, expected_output in test_cases:
        result = solution.lengthOfLastWord(s)
        assert result == expected_output, f"For input '{s}', expected {expected_output}, but got {result}"
    print("All test cases passed!")

test_lengthOfLastWord()
