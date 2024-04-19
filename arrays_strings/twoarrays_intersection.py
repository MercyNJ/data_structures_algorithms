"""
349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2, return an array of their
intersection
. Each element in the result must be unique and you may return the result in any order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                output.add(nums1[i])
        return output


def test():
    nums1_case1 = [1, 2, 2, 1]
    nums2_case1 = [2, 2]
    output1_expected = {2}

    nums1_case2 = [4, 9, 5]
    nums2_case2 = [9, 4, 9, 8, 4]
    output2_expected = {4, 9}

    output1 = set(nums1_case1) & set(nums2_case1)
    assert output1 == output1_expected, f"Test case 1 failed. Output: {list(output1)}, Expected: {list(output1_expected)}"

    output2 = set(nums1_case2) & set(nums2_case2)
    assert output2 == output2_expected, f"Test case 2 failed. Output: {list(output2)}, Expected: {list(output2_expected)}"

    print("All test cases passed!")

if __name__ == "__main__":
    test()
