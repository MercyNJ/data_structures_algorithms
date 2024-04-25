#!/usr/bin/env python3
"""
Module contains implementation for:
345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_s = []

        # Get vowels in s string
        for c in s:
            if c in vowel_list:
                vowels_in_s.append(c)

        # Reverse the obtained list of vowels
        first = 0
        last = len(vowels_in_s) - 1
        while first < last:
            temp = vowels_in_s[first]
            vowels_in_s[first] = vowels_in_s[last]
            vowels_in_s[last] = temp
            first += 1
            last -= 1

        # Reconstruct s with reversed vowels and original non-vowel characters
        result = []
        vowel_index = 0
        for i in range(len(s)):
            if s[i] in vowel_list:
                result.append(vowels_in_s[vowel_index])
                vowel_index += 1
            else:
                result.append(s[i])
        # Join the characters to form the final string
        return ''.join(result)

def test_reverse_vowels():
    test_cases = [
        ("hello", "holle"),
        ("leetcode", "leotcede")
    ]

    solution = Solution()
    for i, (input_str, expected_output) in enumerate(test_cases):
        assert solution.reverseVowels(input_str) == expected_output, f"Test case {i+1} failed"

test_reverse_vowels()
