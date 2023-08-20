"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
"""
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        # add virtual balloons to represent the boundaries
        nums = [1] + nums + [1]
        
        # initialize the dynamic dp array
        # dp[i][j] represents the max coins we can get if we burst from i to j exclude i and j
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # set the default value
        # for the diagonal elements, it must be the value itself, since i == j
        for i in range(1, n+1):
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1]

        # traverse the possible len of j - i
        for length in range(2, n+1):
            for i in range(1, n+2-length):
                j = i + length - 1
                # calculate the max coins we can get if we burst balloon k last
                for k in range(i, j+1):
                    # i <= k <= j
                    # burst k last, means the left of k is nums[i-1] and right is nums[j+1]
                    # so burst k we can get nums[i-1] * nums[k] * nums[j+1]
                    # and we need to consider the coins we can get from i to k-1, and k+1 to j
                    # so we need to add dp[i][k-1] and dp[k+1][j]
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1] * nums[k] * nums[j+1] + dp[k+1][j])
        
        return dp[1][n]