#!/usr/bin/env python3
"""
Module contains implementation for:
2696. Minimum String Length After Removing Substrings
You are given a string s consisting only of uppercase English letters.

You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

Example 1:

Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACDB", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.
"""
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if stack and (stack[-1] + char == "AB" or stack[-1] + char == "CD"):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)

def test_min_length():
    solution = Solution()

    s1 = "ABFCACDB"
    expected_output1 = 2
    assert solution.minLength(s1) == expected_output1, "Test case 1 failed: {}".format(s1)

    s2 = "ACBBD"
    expected_output2 = 5
    assert solution.minLength(s2) == expected_output2, "Test case 2 failed: {}".format(s2)

    print("All test cases passed!")

test_min_length()
