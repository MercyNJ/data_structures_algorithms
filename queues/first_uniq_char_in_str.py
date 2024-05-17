#!/usr/bin/env python3
"""
Module contains implementation for:
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
"""
# Without queue
class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}

        for char in s:
            my_dict[char] = my_dict.get(char, 0) + 1
        for char in s:
            if my_dict[char] == 1:
                return s.index(char)
        return -1

# Using Queue
"""
    Iterate through the string to populate a frequency dictionary (freq_dict) to track the occurrences of each character.
    Store each character along with its index in a queue (queue) to maintain the order of appearance.
    Traverse the queue:
        Dequeue each character and check its frequency in freq_dict.
        If the frequency is 1, return its index, indicating the first non-repeating character.
    If no non-repeating character is found while traversing the queue, return -1.

NB: With defaultdict(int), when you access a key that doesn't exist in the dictionary, it automatically initializes it with the default value of int(), which is 0. This eliminates the need to check if a key exists before incrementing its value.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_dict = defaultdict(int)
        q = deque()

        for i, char in enumerate(s):
            freq_dict[char] += 1
            q.append((char, i)) # Store both char & its index-a tuple
        while q:
            char, index = q.popleft()
            if freq_dict[char] == 1:
                return index
        return -1
