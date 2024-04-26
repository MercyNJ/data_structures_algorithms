#!/usr/bin/env python3
"""
Module contains implementation for:
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Return first string character.
        """
        my_dict = {}

        # count occurences of each character
        for char in s:
            my_dict[char] = my_dict.get(char, 0) + 1

        for char in s:
            if my_dict[char] == 1:
                return s.index(char)
        return -1 

def test_firstUniqChar():
    solution = Solution()

    s1 = "leetcode"
    assert solution.firstUniqChar(s1) == 0

    s2 = "loveleetcode"
    assert solution.firstUniqChar(s2) == 2

    s3 = "aabb"
    assert solution.firstUniqChar(s3) == -1

    print("All test cases passed successfully.")

test_firstUniqChar()


