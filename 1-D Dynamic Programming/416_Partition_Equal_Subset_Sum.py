"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        # if the sum is even, it means that it can be partitioned into two equal subsets
        # if it is odd, it means that it can't
        if total % 2 != 0:
            return False
        
        target = total // 2
        # initialize a dp array to record if is possible to find a subset of nums that sum is equal to i
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]

        return dp[target]