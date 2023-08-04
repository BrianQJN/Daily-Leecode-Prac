"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # define the max_reach to record the max index jump can reach
        max_reach = 0

        # traverse the nums to see where we can reach at each position
        for i in range(n):
            # if cur index is greater than the max index we can jump to, return False
            if i > max_reach:
                return False
            # else update the max_reach
            max_reach = max(max_reach, i + nums[i])

        return True
            