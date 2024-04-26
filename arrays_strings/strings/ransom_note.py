#!/usr/bin/env python3
"""
Module contains implementation for:
383. Ransom Note
Given two strings ransomNote and magazine, return true if
ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determine if ransomNote can be constructed with letters from magazine.
        """
        ransomNote_count = {}
        magazine_count = {}

        for char in ransomNote:
            ransomNote_count[char] = ransomNote_count.get(char, 0) + 1

        for char in magazine:
            magazine_count[char] = magazine_count.get(char, 0) + 1

        for char, count in ransomNote_count.items():
            if char not in magazine or magazine_count[char] < count:
                return False
        return True

def test_canConstruct():
    solution = Solution()

    ransomNote1 = "a"
    magazine1 = "b"
    assert solution.canConstruct(ransomNote1, magazine1) == False

    ransomNote2 = "aa"
    magazine2 = "ab"
    assert solution.canConstruct(ransomNote2, magazine2) == False

    ransomNote3 = "aa"
    magazine3 = "aab"
    assert solution.canConstruct(ransomNote3, magazine3) == True

    ransomNote4 = "aab"
    magazine4 = "baa"
    assert solution.canConstruct(ransomNote4, magazine4) == True

    print("All test cases passed successfully.")

test_canConstruct()

