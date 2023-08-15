"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        max_sum = sum(nums)

        # boundary conditions, if the abs of target is greater than the sum of nums, means no mattet how to combine, no way
        # and if (target + max_sum) % 2 != 0 means we can't find combinations that sum are (target + max_sum) / 2
        if abs(target) > max_sum or (target + max_sum) % 2 != 0:
            return 0
        
        target = (target + max_sum) // 2

        # initialize the dp array to record the ways to sum to i
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]

        return dp[-1]