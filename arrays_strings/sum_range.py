"""
303. Range Sum Query - Immutable
Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).



Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
"""
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = nums
        for i in range(len(nums)-1):
            self.preSum[i+1] += self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.preSum[right]
        return self.preSum[right] - self.preSum[left-1]

def test():
    # Test case 1
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    outputs = [numArray.sumRange(0, 2), numArray.sumRange(2, 5), numArray.sumRange(0, 5)]
    expected_outputs = [1, -1, -3]

    # Test case 2
    numArray2 = NumArray([1, 2, 3, 4, 5])
    outputs2 = [numArray2.sumRange(1, 3), numArray2.sumRange(0, 4)]
    expected_outputs2 = [9, 15]

    # Printing results for test case 1
    print("Test Case 1:")
    for i in range(len(outputs)):
        print("Output{}:".format(i+1), outputs[i], "Expected{}:".format(i+1), expected_outputs[i])

    # Printing results for test case 2
    print("\nTest Case 2:")
    for i in range(len(outputs2)):
        print("Output{}:".format(i+4), outputs2[i], "Expected{}:".format(i+4), expected_outputs2[i])

if __name__ == "__main__":
    test()
