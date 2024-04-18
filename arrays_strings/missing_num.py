"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.
"""
from typing import List

#my implemetation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        for i in range(n):
            if i not in nums:
                return i
        return i

def test_missing_number():
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    solution = Solution()
    for nums, expected_output in test_cases:
        output = solution.missingNumber(nums)
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    print("All test cases passed!")

test_missing_number()

#alternative efficient implementation
"""Formula: (n×(n+1))//2(n×(n+1))//2 for sum of numbers from 0 to nn.
Missing number: Difference between sequence sum and sum of nums list."""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
