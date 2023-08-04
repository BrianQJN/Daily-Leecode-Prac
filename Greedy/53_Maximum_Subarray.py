"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Using the dynamic programming to solve the problem
        n = len(nums)
        # initialize a dp array to record the max sum in the 0~ith num
        dp = [0] * n
        dp[0], max_sum = nums[0], nums[0]

        # ith max sum is max of the cur nums[i] or the dp[i-1]+nums[i]
        # e.g. dp[i-1] = -2, nums[i] = 2, so dp[i] = max(dp[i-1]+nums[i], nums[i]) not dp[i-1]+nums[i]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # using the greedy programming to solve the problem
        n = len(nums)
        cur_sum = max_sum = nums[0]

        # e.g. cur_sum = -1, nums[i] = 2, so we should move the subarray head to nums[i] to get greater sum
        # so cur_sum = max(cur_sum + nums[i], nums[i]) not cur_sum + nums[i]
        for i in range(1, n):
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)

        return max_sum