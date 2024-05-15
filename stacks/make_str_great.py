#!/usr/bin/env python3
"""
Module contains implementation for:
1544. Make The String Great
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:
    0 <= i <= s.length - 2
    s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.
Example 1:
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
"""
# STEPS TO FOLLOW
"""    Initialize an empty stack to keep track of characters.
    Iterate through each character in the input string.
    For each character:
        If the stack is not empty and the current character and the top character of the stack form a pair of adjacent characters that violate the condition (one lowercase and one uppercase of the same letter, or vice versa), pop the top character from the stack.
        Otherwise, push the current character onto the stack.
    After iterating through all characters, concatenate the characters remaining in the stack to form the resulting string.
    """
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        result = ''

        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        for char in stack:
            result += char
        return result

# Using join
def makeGood_two(self, s: str) -> str:
    stack = []
    
    for char in s:
        if stack and abs(ord(char) - ord(stack[-1])) == 32:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)


def test_makeGood():
    sol = Solution()

    input1 = "leEeetcode"
    assert sol.makeGood(input1) == "leetcode"

    input2 = "abBAcC"
    assert sol.makeGood(input2) == ""

    input3 = "s"
    assert sol.makeGood(input3) == "s"

    print("All test cases passed.")

test_makeGood()
