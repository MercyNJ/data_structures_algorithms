#!/usr/bin/env python3
"""
Module contains implementation for:
496. Next Greater Element I
he next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1))
        return result

def test_nextGreaterElement():
    s = Solution()

    nums1_1 = [4, 1, 2]
    nums2_1 = [1, 3, 4, 2]
    expected_output_1 = [-1, 3, -1]
    output_1 = s.nextGreaterElement(nums1_1, nums2_1)
    assert output_1 == expected_output_1, "Test Case 1 Failed: Expected {}, but got {}".format(expected_output_1, output_1)

    nums1_2 = [2, 4]
    nums2_2 = [1, 2, 3, 4]
    expected_output_2 = [3, -1]
    output_2 = s.nextGreaterElement(nums1_2, nums2_2)
    assert output_2 == expected_output_2, "Test Case 2 Failed: Expected {}, but got {}".format(expected_output_2, output_2)

    print("All test cases passed!")

test_nextGreaterElement()
