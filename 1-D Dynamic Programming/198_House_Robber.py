"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return nums[0]

        # initialize the dp to record how much money have been robbed 
        dp = [0] * n

        # for first house, can only rob itself, but for second, we can choose rob itself or last one, so choose the max one between them
        dp[0], dp[1] = nums[0], max(nums[1], nums[0])

        # for each house, we can choose to rob itself and add dp[i-2] we have robbed to count total, or choose to rob last house and get total in robbing last house
        # choose max between two robbing plans
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[n-1]