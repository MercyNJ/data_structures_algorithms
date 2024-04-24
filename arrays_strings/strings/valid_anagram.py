#!/usr/bin/env python3
"""
Module contains implementation for:
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""
# my implementation
class Solution:
    """
    Check if given strings are anagrams of each other.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {char: s.count(char) for char in s}
        t_dict = {c: t.count(c) for c in t}

        return (all(char in s for char in t) and
        all(s_dict[ch] == t_dict[ch] for ch in s))

def test_isAnagram():
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aacc", "ccac", False)
    ]
    
    solution = Solution()
    
    for s, t, expected_output in test_cases:
        result = solution.isAnagram(s, t)
        assert result == expected_output, "Test case failed! Input: s = {}, t = {}, Expected output: {}, Output: {}".format(s, t, expected_output, result)
    
    print("All test cases passed successfully!")

test_isAnagram()


# Alternative implemntation 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

# Alternative implemntation 2
# dictionary comparison doesnt necessarily conside order as long as keys and values match
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they can't be anagrams
        if len(s) != len(t):
            return False

        # Initialize dictionaries to count occurrences of characters in both strings
        s_count = {}
        t_count = {}

        # Count occurrences of characters in string s, 0 as default
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1

        # Count occurrences of characters in string t
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        # Check if the dictionaries are equal
        return s_count == t_count

# Test cases
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))         # Output: False


