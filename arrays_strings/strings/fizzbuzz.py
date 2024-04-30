#!/usr/bin/env python3
"""
Module contains implementation for:
412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
"""
from typing import List

# my implementation
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

def test_fizzBuzz():
    solution = Solution()

    n1 = 3
    output1 = ["1", "2", "Fizz"]
    assert solution.fizzBuzz(n1) == output1, f"Test case 1 failed: expected {output1}, got {solution.fizzBuzz(n1)}"

    n2 = 5
    output2 = ["1", "2", "Fizz", "4", "Buzz"]
    assert solution.fizzBuzz(n2) == output2, f"Test case 2 failed: expected {output2}, got {solution.fizzBuzz(n2)}"

    n3 = 15
    output3 = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    assert solution.fizzBuzz(n3) == output3, f"Test case 3 failed: expected {output3}, got {solution.fizzBuzz(n3)}"

    print("All test cases passed!")

test_fizzBuzz()
