"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""
from collections import deque


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # initialize the dp array to record the min number of coins to reach amount i
        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        # loop through each coin and update the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # if dp[amount] is still greater than amount, means there is no combination, return -1
        return dp[amount] if dp[amount] <= amount else -1
    
    def coinChange2(self, coins, amount):
        # using a queue to record cur reached amount and how many coins have used
        queue = deque([(0, 0)])
        # using a set to record the amount we have visited
        visited = set()

        while queue:
            cur_amount, steps = queue.popleft()

            # return the number of coins we have used if we reached the amount
            if cur_amount == amount:
                return steps
            
            # traverse the coins, and looking for the new amount we can reach
            # if we didn't visited this amount, and the new amount is less than the amount
            # we add it to the queue to do next level BFS
            for coin in coins:
                new_amount = cur_amount + coin
                if new_amount <= amount and new_amount not in visited:
                    queue.append([new_amount, steps + 1])
                    visited.add(new_amount)

        return -1
