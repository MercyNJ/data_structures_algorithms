"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Solution logic:
        We can divide the problem into two subproblems:
        Find the maximum profit for the first transaction from day 0 to day i.
        Find the maximum profit for the second transaction from day i to the end.

    We iterate through the prices list and calculate the maximum profit for the first transaction for each day.

    We then iterate through the prices list in reverse order and calculate the maximum profit for the second transaction for each day.

    We combine the maximum profits from both transactions and return the maximum value.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        max_profit = 0

        # Calculate maximum profit for the first transaction
        max_profit_forward = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            max_profit_forward[i] = max(max_profit_forward[i - 1], prices[i] - min_price)

        # Calculate maximum profit for the second transaction
        max_profit_backward = [0] * n
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            max_profit_backward[i] = max(max_profit_backward[i + 1], max_price - prices[i])

        # Combine maximum profits from both transactions
        for i in range(n):
            max_profit = max(max_profit, max_profit_forward[i] + max_profit_backward[i])

        return max_profit

def test_maxProfit():
    solution = Solution()

    input_1 = [3, 3, 5, 0, 0, 3, 1, 4]
    expected_output_1 = 6
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
