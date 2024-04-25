#!/usr/bin/env python3
"""
Module contains implementation for:
344. Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1

        while first < last:
            temp = s[first]
            s[first] = s[last]
            s[last] = temp
            first += 1
            last -= 1

s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]

solution = Solution()

solution.reverseString(s1)
assert s1 == ["o", "l", "l", "e", "h"], "Test Case 1 failed"

solution.reverseString(s2)
assert s2 == ["h", "a", "n", "n", "a", "H"], "Test Case 2 failed"

print("All test cases passed successfully.")

#inplace approach 2- recursion
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse_helper(left, right):
            if left < right:
                # Swap characters at left and right pointers
                s[left], s[right] = s[right], s[left]
                # Move the pointers towards the center
                reverse_helper(left + 1, right - 1)

        # initial call
        reverse_helper(0, len(s) - 1)

