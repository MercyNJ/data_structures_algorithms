"""
Sorting an array containing both numbers and strings.
Given a list that contains both integers and strings, sort it such that:
- Numbers appear first, sorted in ascending order.
- Strings appear after numbers, sorted in alphabetical order.

Example 1:
Input: arr = [3, "apple", 1, "banana", 2, "cherry"]
Output: [1, 2, 3, 'apple', 'banana', 'cherry']
"""

from typing import List, Union

class Solution:
    def sortMixedArray(self, arr: List[Union[int, str]]) -> List[Union[int, str]]:
        # Separate numbers and strings into different lists
        numbers = []
        strings = []

        for item in arr:
            if isinstance(item, int):
                numbers.append(item)  # Store numbers separately
            else:
                strings.append(item)  # Store strings separately
        
        # Implementing Bubble Sort for numbers
        for i in range(len(numbers)):
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:  
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # Swap numbers
        
        # Implementing Bubble Sort for strings
        for i in range(len(strings)):
            for j in range(0, len(strings) - i - 1):
                if strings[j] > strings[j + 1]:  
                    strings[j], strings[j + 1] = strings[j + 1], strings[j]  # Swap strings
        
        # Combine sorted numbers and strings
        return numbers + strings

def test_sortMixedArray():
    solution = Solution()

    input_1 = [3, "apple", 1, "banana", 2, "cherry"]
    output_1 = solution.sortMixedArray(input_1)
    print("Input:", input_1)
    print("Output:", output_1)
    print()

    input_2 = [5, "dog", 2, "cat", 8, "elephant"]
    output_2 = solution.sortMixedArray(input_2)
    print("Input:", input_2)
    print("Output:", output_2)
    print()

    input_3 = ["zebra", "monkey", 10, 3, 5]
    output_3 = solution.sortMixedArray(input_3)
    print("Input:", input_3)
    print("Output:", output_3)
    print()

    input_4 = [1, 4, 2, 3]
    output_4 = solution.sortMixedArray(input_4)
    print("Input:", input_4)
    print("Output:", output_4)
    print()

    input_5 = ["apple", "banana", "cherry"]
    output_5 = solution.sortMixedArray(input_5)
    print("Input:", input_5)
    print("Output:", output_5)
    print()

test_sortMixedArray()

