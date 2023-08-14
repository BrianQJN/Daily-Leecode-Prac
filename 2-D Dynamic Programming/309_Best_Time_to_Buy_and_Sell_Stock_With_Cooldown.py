"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0
        
        # initialize two dp arrays
        # buy to record if we possess the stock at day i
        # sell to record if we don't have the stock at day i
        buy = [0] * n
        sell = [0] * n

        # initialize the first day
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[0] = 0
        sell[1] = max(0, prices[1]-prices[0])

        for i in range(2, n):
            # apply dynamic status transition equations
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        return sell[-1]