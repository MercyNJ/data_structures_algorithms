#!/usr/bin/env python3
"""
Module contains implementation for:
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()
        # filters out non-alphanumeric chars
        filtered_str = "".join(c for c in lower_str if c.isalnum())

        if filtered_str == filtered_str[::-1]:
            return True
        return False

# Test cases
solution = Solution()
assert solution.isPalindrome("") == True
assert solution.isPalindrome("a") == True
assert solution.isPalindrome("A man, a plan, a canal: Panama") == True
assert solution.isPalindrome("résumé") == False 

print("All tests passed!")

