#!/usr/bin/env python3
"""
Module contains implementation for:
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize a dictionary to store the frequency of each character
        char_count = {}

        # Count the frequency of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Initialize a variable to store the length of the longest palindrome
        longest_length = 0

        # Initialize a variable to keep track of whether an odd count of characters has been encountered
        has_odd = False

        # Iterate through the frequency counts of each character
        for count in char_count.values():
            # If the count is even, add it to the length of the longest palindrome
            if count % 2 == 0:
                longest_length += count
            # If the count is odd, subtract 1 and add it to the length of the longest palindrome
            # Also, set has_odd to True to keep track that an odd count has been encountered
            else:
                longest_length += count - 1
                has_odd = True

        # If an odd count of characters has been encountered, add 1 to the length of the longest palindrome
        if has_odd:
            longest_length += 1

        # Return the length of the longest palindrome
        return longest_length

def test_longestPalindrome():
    solution = Solution()

    s1 = "abccccdd"
    output1 = 7
    assert solution.longestPalindrome(s1) == output1, f"Test case 1 failed: expected {output1}, got {solution.longestPalindrome(s1)}"

    s2 = "a"
    output2 = 1
    assert solution.longestPalindrome(s2) == output2, f"Test case 2 failed: expected {output2}, got {solution.longestPalindrome(s2)}"

    print("All test cases passed!")

test_longestPalindrome()
