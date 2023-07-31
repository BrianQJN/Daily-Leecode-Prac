"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        
        # initialize an array dp to store the number of distinct ways to reach the each stair
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        # use a loop to calculate the number of distinct ways to reach each stair
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
