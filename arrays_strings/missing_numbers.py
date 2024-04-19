"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:

Input: nums = [1,1]
Output: [2]
"""
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        disappeared_numbers = []

        for i in range(1, n+1):
            if i not in nums_set:
                disappeared_numbers.append(i)

        return disappeared_numbers

def test_findDisappearedNumbers():
    solution = Solution()
    
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    assert solution.findDisappearedNumbers(nums1) == [5, 6], "Test case 1 failed"
    nums2 = [1, 1]
    assert solution.findDisappearedNumbers(nums2) == [2], "Test case 2 failed"
    
    print("All test cases passed!")

test_findDisappearedNumbers()

