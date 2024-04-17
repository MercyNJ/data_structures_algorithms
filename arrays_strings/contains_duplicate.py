"""
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        #if loop completes without finding duplicates
        return False

def test_containsDuplicate():
    solution = Solution()

    input_1 = [1, 2, 3, 1]
    expected_output_1 = True
    output_1 = solution.containsDuplicate(input_1)
    assert output_1 == expected_output_1, "Test case 1 failed: Expected {}, but got {}".format(expected_output_1, output_1)

    input_2 = [1, 2, 3, 4]
    expected_output_2 = False
    output_2 = solution.containsDuplicate(input_2)
    assert output_2 == expected_output_2, "Test case 2 failed: Expected {}, but got {}".format(expected_output_2, output_2)

    input_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    expected_output_3 = True
    output_3 = solution.containsDuplicate(input_3)
    assert output_3 == expected_output_3, "Test case 3 failed: Expected {}, but got {}".format(expected_output_3, output_3)

    input_4 = [2, 14, 18, 22, 22]
    expected_output_4 = True
    output_4 = solution.containsDuplicate(input_4)
    assert output_4 == expected_output_4, "Test case 4 failed: Expected {}, but got {}".format(expected_output_4, output_4)

    print("All test cases passed!")

test_containsDuplicate()

