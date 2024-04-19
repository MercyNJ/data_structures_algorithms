"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
from typing import List

# Solution 1 using counter
# ounts the occurrences of each element in a list and returns
#a dictionary with the elements as keys and their counts as values

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)

        output = []

        for num in nums2:
            if num in counts and counts[num] > 0:
                output.append(num)
                counts[num] -= 1

        return output

# Solution 2 -create dictionry
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        output = []

        for num in nums2:
            if num in counts and counts[num] > 0:
                output.append(num)
                counts[num] -= 1

        return output

def test_intersect():
    # Test case 1
    nums1_case1 = [1, 2, 2, 1]
    nums2_case1 = [2, 2]
    output1_expected = [2, 2]

    # Test case 2
    nums1_case2 = [4, 9, 5]
    nums2_case2 = [9, 4, 9, 8, 4]
    output2_expected = [4, 9]

    # Test case 3
    nums1_case3 = [1, 2, 2, 1]
    nums2_case3 = [2]
    output3_expected = [2]

    # Testing
    sol = Solution()
    
    output1 = sol.intersect(nums1_case1, nums2_case1)
    assert output1 == output1_expected, f"Test case 1 failed. Output: {output1}, Expected: {output1_expected}"
    
    output2 = sol.intersect(nums1_case2, nums2_case2)
    assert output2 == output2_expected, f"Test case 2 failed. Output: {output2}, Expected: {output2_expected}"

    output3 = sol.intersect(nums1_case3, nums2_case3)
    assert output3 == output3_expected, f"Test case 3 failed. Output: {output3}, Expected: {output3_expected}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_intersect()

