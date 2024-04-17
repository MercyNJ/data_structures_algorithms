"""
122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Solution logic:
        We calculate the profit for each day by subtracting the current price from the previous day's price.
    If the profit is positive (meaning the price increased from the previous day), we add it to the max_profit.
    We repeat this process for all days in the prices list.
    Finally, we return the max_profit, which represents the maximum profit that can be achieved by buying and/or selling the stock on different days.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit

        return max_profit

def test_maxProfit():
    solution = Solution()

    input_1 = [7, 1, 5, 3, 6, 4]
    expected_output_1 = 7
    output_1 = solution.maxProfit(input_1)
    assert output_1 == expected_output_1, "Test case 1 failed: Expected {}, but got {}".format(expected_output_1, output_1)

    input_2 = [1, 2, 3, 4, 5]
    expected_output_2 = 4
    output_2 = solution.maxProfit(input_2)
    assert output_2 == expected_output_2, "Test case 2 failed: Expected {}, but got {}".format(expected_output_2, output_2)

    input_3 = [7, 6, 4, 3, 1]
    expected_output_3 = 0
    output_3 = solution.maxProfit(input_3)
    assert output_3 == expected_output_3, "Test case 3 failed: Expected {}, but got {}".format(expected_output_3, output_3)

    print("All test cases passed!")

test_maxProfit()
