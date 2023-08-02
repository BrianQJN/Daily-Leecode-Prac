"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        # initialize a dp array to record the maximum product
        max_dp = [0] * n
        # initialize a dp array to record the minimum product
        min_dp = [0] * n

        max_dp[0] = min_dp[0] = nums[0]
        res = nums[0]

        for i in range(1, n):
            # if nums[i] is positive
            if nums[i] > 0:
                # max product = cur num * last max product or itself
                max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i])
                # min product = cur num * last min product or itself
                min_dp[i] = min(nums[i], min_dp[i - 1] * nums[i])
            elif nums[i] < 0:
                # max product = cur num * last min product or itself
                max_dp[i] = max(nums[i], min_dp[i - 1] * nums[i])
                # min product = cur num * last max product or itself
                min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i])
            else:
                max_dp[i] = min_dp[i] = 0

            res = max(res, max_dp[i])

        return res