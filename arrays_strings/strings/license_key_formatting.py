#!/usr/bin/env python3
"""
Module contains implementation for:
482. License Key Formatting
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.
Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
"""
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        dash = '-'
        s_modified = [c for c in s if c != dash]

        n = len(s_modified)
        result = ""
        count = 0

        for j in range(n - 1, -1, -1):
            if count == k:  # Insert a dash after every k characters
                result = dash + result
                count = 0  # Reset the counter
            result = s_modified[j].upper() + result
            count += 1

        return result

def test_licenseKeyFormatting():
    solution = Solution()

    s1 = "5F3Z-2e-9-w"
    k1 = 4
    expected_output_1 = "5F3Z-2E9W"
    result_1 = solution.licenseKeyFormatting(s1, k1)
    assert result_1 == expected_output_1, f"Test case 1 failed: Expected {expected_output_1}, but got {result_1}"

    s2 = "2-5g-3-J"
    k2 = 2
    expected_output_2 = "2-5G-3J"
    result_2 = solution.licenseKeyFormatting(s2, k2)
    assert result_2 == expected_output_2, f"Test case 2 failed: Expected {expected_output_2}, but got {result_2}"

    print("All test cases passed!")

test_licenseKeyFormatting()

#Alternative Implementation
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Step 1: Remove dashes and convert to uppercase
        s = s.replace('-', '').upper()

        # Step 2: Reverse the string
        s = s[::-1]

        # Step 3: Generate substrings of length k
        parts = [s[i:i+k] for i in range(0, len(s), k)]

        # Step 4: Join the parts together with dashes and reverse the string again
        return '-'.join(parts)[::-1]
