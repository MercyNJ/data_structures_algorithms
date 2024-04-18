"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1
def test_move_zeroes():
    solution = Solution()
    
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0], "Test case 1 failed"
    
    nums2 = [0]
    solution.moveZeroes(nums2)
    assert nums2 == [0], "Test case 2 failed"
    
    print("All test cases passed")

test_move_zeroes()

