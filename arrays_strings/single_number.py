"""
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1
"""
from typing import List

#My implementation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]
            else:
                None


def test_singleNumber():
    solution = Solution()

    input_1 = [2, 2, 1]
    expected_output_1 = 1
    output_1 = solution.singleNumber(input_1)
    assert output_1 == expected_output_1, "Test case 1 failed: Expected {}, but got {}".format(expected_output_1, output_1)

    input_2 = [4, 1, 2, 1, 2]
    expected_output_2 = 4
    output_2 = solution.singleNumber(input_2)
    assert output_2 == expected_output_2, "Test case 2 failed: Expected {}, but got {}".format(expected_output_2, output_2)

    input_3 = [1]
    expected_output_3 = 1
    output_3 = solution.singleNumber(input_3)
    assert output_3 == expected_output_3, "Test case 3 failed: Expected {}, but got {}".format(expected_output_3, output_3)

    print("All test cases passed!")

test_singleNumber()

#ALTERNATIVE APPROACH
"""
After iterating through all numbers in nums, answer will contain the result of XORing all numbers together.
Since XORing a number with itself cancels out (resulting in 0), and XORing 0 with any number
returns the number itself, the final value of answer will be the number that appears only once in the list."""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer
