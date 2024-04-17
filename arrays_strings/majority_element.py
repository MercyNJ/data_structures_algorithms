"""
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array."""
#my implemntation
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums.count(nums[i]) > (n // 2):
                return nums[i]
            else:
                continue

def test_majorityElement():
    solution = Solution()

    input_1 = [3, 2, 3]
    expected_output_1 = 3
    output_1 = solution.majorityElement(input_1)
    assert output_1 == expected_output_1, "Test case 1 failed: Expected {}, but got {}".format(expected_output_1, output_1)

    input_2 = [2, 2, 1, 1, 1, 2, 2]
    expected_output_2 = 2
    output_2 = solution.majorityElement(input_2)
    assert output_2 == expected_output_2, "Test case 2 failed: Expected {}, but got {}".format(expected_output_2, output_2)

    input_3 = [6, 5, 5]
    expected_output_3 = 5
    output_3 = solution.majorityElement(input_3)
    assert output_3 == expected_output_3, "Test case 3 failed: Expected {}, but got {}".format(expected_output_3, output_3)

    print("All test cases passed!")

test_majorityElement()

#alternative implementation
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
