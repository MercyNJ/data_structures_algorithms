#!/usr/bin/env python3
"""
Module contains implementation for:

13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        """ Convert Given Roman numeral to integer. """
        result = []
        basic_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
        }
        special_numerals = {"IV": 4,
                            "IX": 9,
                            "XL": 40,
                            "XC": 90,
                            "CD": 400,
                            "CM": 900
        }

        symbols = list(s)
        length = len(symbols)
        i = length - 1
        # iterate from backwards
        while i >= 0:
            combined_symbol = symbols[i - 1] + symbols[i]
            if i > 0 and combined_symbol in special_numerals:
                result.append(special_numerals[combined_symbol])
                i -= 2
            elif symbols[i] in basic_numerals:
                result.append(basic_numerals[symbols[i]])
                i -= 1
        result_int = list(map(int, result))
        total_sum = sum(result_int)
        return total_sum

def test_roman_to_int():
    solution = Solution()
    
    input_1 = "III"
    expected_output_1 = 3
    output_1 = solution.romanToInt(input_1)
    assert output_1 == expected_output_1, "Test case 1 failed: Expected {}, but got {}".format(expected_output_1, output_1)

    input_2 = "LVIII"
    expected_output_2 = 58
    output_2 = solution.romanToInt(input_2)
    assert output_2 == expected_output_2, "Test case 2 failed: Expected {}, but got {}".format(expected_output_2, output_2)

    input_3 = "MCMXCIV"
    expected_output_3 = 1994
    output_3 = solution.romanToInt(input_3)
    assert output_3 == expected_output_3, "Test case 3 failed: Expected {}, but got {}".format(expected_output_3, output_3)

    print("All test cases passed!")

test_roman_to_int()
