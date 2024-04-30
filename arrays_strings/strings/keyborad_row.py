#!/usr/bin/env python3
"""
Module contains implementation for:
500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl", and
    the third row consists of the characters "zxcvbnm".
Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define rows of the keyboard
        keyboard = {
            'qwertyuiop': 1,
            'asdfghjkl': 2,
            'zxcvbnm': 3
        }

        # List to store words that can be typed using one row
        result = []

        # Iterate through each word
        for word in words:
            # Get the row of the first character in the word
            first_char_row = 0
            for row_chars, row_num in keyboard.items():
                if word[0].lower() in row_chars:
                    first_char_row = row_num
                    break

            # Check if all characters belong to the same row
            same_row = True
            for char in word:
                char_row = 0
                for row_chars, row_num in keyboard.items():
                    if char.lower() in row_chars:
                        char_row = row_num
                        break
                if char_row != first_char_row:
                    same_row = False
                    break

            if same_row:
                result.append(word)

        return result

def test_findWords():
    solution = Solution()

    words_1 = ["Hello", "Alaska", "Dad", "Peace"]
    expected_output_1 = ["Alaska", "Dad"]
    assert solution.findWords(words_1) == expected_output_1

    words_2 = ["omk"]
    expected_output_2 = []
    assert solution.findWords(words_2) == expected_output_2

    words_3 = ["adsdf", "sfd"]
    expected_output_3 = ["adsdf", "sfd"]
    assert solution.findWords(words_3) == expected_output_3

    print("All test cases passed!")

test_findWords()
