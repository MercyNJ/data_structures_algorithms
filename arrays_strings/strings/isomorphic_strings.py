#!/usr/bin/env python3
"""
Module contains implementation for:
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
Example 1:

Input: s = "egg", t = "add"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Mapping to store the mapping of characters from s to t
        mapping_s_to_t = {}
        # Set to keep track of characters already mapped in t
        mapped_chars_t = set()

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # If char_s has not been mapped yet, map it to char_t
            if char_s not in mapping_s_to_t:
                # Check if char_t has already been mapped to another character
                if char_t in mapped_chars_t:
                    return False
                mapping_s_to_t[char_s] = char_t
                mapped_chars_t.add(char_t)
            # If char_s has been mapped, check if the mapping is consistent
            elif mapping_s_to_t[char_s] != char_t:
                return False

        return True

# Test cases
solution = Solution()
print(solution.isIsomorphic("egg", "add"))  # Output: True
print(solution.isIsomorphic("foo", "bar"))  # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True
