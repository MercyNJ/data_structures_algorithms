#!/usr/bin/env python3
"""
Module contains implementation for:
1475. Final Prices With a Special Discount in a Shop
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

Example 1:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
"""
from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                    discounted_index = stack.pop()
                    prices[discounted_index] -= price
            stack.append(i)
        return prices

def test_final_prices():
    sol = Solution()
    
    prices1 = [8, 4, 6, 2, 3]
    assert sol.finalPrices(prices1) == [4, 2, 4, 2, 3]
    
    prices2 = [1, 2, 3, 4, 5]
    assert sol.finalPrices(prices2) == [1, 2, 3, 4, 5]
    
    prices3 = [10, 1, 1, 6]
    assert sol.finalPrices(prices3) == [9, 0, 1, 6]
    
    print("All test cases passed.")

test_final_prices()

# Without using enumerate
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        i = 0
        while i < n:
            price = prices[i]
            while stack and prices[stack[-1]] >= price:
                discounted_index = stack.pop()
                prices[discounted_index] -= price
            stack.append(i)
            i += 1
        return prices
