"""
228. Summary Ranges
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b
Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

logic:each range in the output should cover all the numbers exactly once, without any gaps or overlapswe don't form a single range covering the entire span from 0 to 7, as it would include numbers not present in the input array.
"""
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []

        if not nums:
            return []

        start = end = nums[0]
        for i in range(1, len(nums)):
            # check if current num is consecutivewith the previous one
            if nums[i] - nums[i - 1] == 1:
                end = nums[i]
            #end of a range either one num or multiple    
            else:
                if start == end:
                    output.append(str(start))
                else:
                    output.append(str(start) + "->" + str(end))
                # # Update the start and end pointers for the new range
                start = end = nums[i]
        # After loop, append the last range (or single number) to the output list
        if start == end:
            output.append(str(start))
        else:
            output.append(str(start) + "->" + str(end))
        return output

def test_summary_ranges():
    test_cases = [
        ([0,1,2,4,5,7], ["0->2", "4->5", "7"]),
        ([0,2,3,4,6,8,9], ["0", "2->4", "6", "8->9"]),
    ]

    solution = Solution()
    for nums, expected_output in test_cases:
        output = solution.summaryRanges(nums)
        assert output == expected_output, f"Expected: {expected_output}, but got: {output}"

    print("All test cases passed!")

test_summary_ranges()


