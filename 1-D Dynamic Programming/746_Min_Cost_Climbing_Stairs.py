"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)

        # initialize the dp array with len n+1 to record spend to reach this step
        dp = [0] * (n + 1)

        dp[0], dp[1] = cost[0], cost[1]

        # calculate the minimum cost to reach each step
        for i in range(2, n):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]

        return min(dp[n-1], dp[n-2])