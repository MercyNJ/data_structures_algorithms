#!/usr/bin/env python3
"""
Module contains implementation for:
290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s.
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Find if string follows given pattern.
        """
        s_words = s.split()
        len_pattern = len(pattern)
        len_s_words = len(s_words)

        if len_pattern != len_s_words:
            return False

        # dict to store mapping betwn chars in pattern and words in s
        pattern_mappings = {}
        # set keep track of mapped words in s
        mapped_words_s = set()

        for i in range(len(pattern)):
            char_pattern = pattern[i]
            word_s = s_words[i]

            # If char is not in the dict
            if char_pattern not in pattern_mappings:
                #if word has been mapped to diff char b4
                if word_s in mapped_words_s:
                    return False
                pattern_mappings[char_pattern] = word_s
                mapped_words_s.add(word_s)
            elif pattern_mappings[char_pattern] != word_s:
                return False
        return True

def test_wordPattern():
    solution = Solution()
    
    pattern1 = "abba"
    s1 = "dog cat cat dog"
    expected_output1 = True
    assert solution.wordPattern(pattern1, s1) == expected_output1
    
    pattern2 = "abba"
    s2 = "dog cat cat fish"
    expected_output2 = False
    assert solution.wordPattern(pattern2, s2) == expected_output2
    
    pattern3 = "aaaa"
    s3 = "dog cat cat dog"
    expected_output3 = False
    assert solution.wordPattern(pattern3, s3) == expected_output3
    
    print("All test cases passed!")

test_wordPattern()
