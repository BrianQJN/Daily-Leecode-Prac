"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # initialize the dp array to record the number of nums that is less than nums[i]
        # since the num itself can be treated as an increasing subsequence
        dp = [1] * n

        for i in range(1, n):
            for j in range(0, i):
                # if nums[i] is greater than nums[j], dp[j] is counts of nums less than nums[j]
                # so dp[i] = dp[j] + 1, 1 means the num[j] itself
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)