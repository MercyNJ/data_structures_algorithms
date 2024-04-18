"""
219. Contains Duplicate II
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
"""
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        elem_indices = {}

        for i, num in enumerate(nums):
            if num in elem_indices and abs(i - elem_indices[num]) <= k:
                return True
            elem_indices[num] = i
        return False

def test_contains_nearby_duplicate():
    test_cases = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]

    solution = Solution()
    for nums, k, expected_output in test_cases:
        output = solution.containsNearbyDuplicate(nums, k)
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    print("All test cases passed!")

test_contains_nearby_duplicate()

