#!/usr/bin/env python3
"""
Module contains implementation for:
Check if pair with given Sum exists in Array (Two Sum)
Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x.

Examples:

    Input: arr[] = {0, -1, 2, -3, 1}, x= -2
    Output: Yes
"""
# Approach 1 -Using Hashmap
from typing import List

class TwoSumChecker:
    def check_pair_with_sum(self, A: List[int], x: int) -> bool:
        seen = set()
        for elem in A:
            complement = x - elem
            if complement in seen:
                return True
            seen.add(elem)
        return False

def test_check_pair_with_sum():
    checker = TwoSumChecker()
    
    arr1 = [0, -1, 2, -3, 1]
    x1 = -2
    result1 = checker.check_pair_with_sum(arr1, x1)
    passed1 = result1 == True
    print("Test case 1 passed:", passed1)

    arr2 = [1, -2, 1, 0, 5]
    x2 = 0
    result2 = checker.check_pair_with_sum(arr2, x2)
    passed2 = result2 == False
    print("Test case 2 passed:", passed2)
    
test_check_pair_with_sum()

# Approach 2 - Naive approach
class TwoSumChecker:
    def check_pair_with_sum(self, A: List[int], x: int) -> bool:
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] == x:
                    return True
        return False

