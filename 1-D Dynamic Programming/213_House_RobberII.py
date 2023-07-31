"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
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

        if n == 2:
            return max(nums[0], nums[1])

        def rob_range(start, end):
            cur_nums = nums[start:end]
            m = len(cur_nums)
            dp = [0] * m
            dp[0] = cur_nums[0]
            dp[1] = max(cur_nums[0], cur_nums[1])
            for i in range(2, m):
                dp[i] = max(cur_nums[i] + dp[i-2], dp[i-1])
            return dp[m-1]
        
        return max(rob_range(0, n-1), rob_range(1, n))
        