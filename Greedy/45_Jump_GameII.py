"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

· 0 <= j <= nums[i] and
· i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # initialize max_reach to record the max index we can reach from cur position
        # end to record the boundary of cur jump
        # steps to record jump times
        max_reach, end, steps = 0, 0, 0

        for i in range(0, n-1):
            # still need to get the max index we can reach for this jump
            max_reach = max(max_reach, i + nums[i])
            # if i reach last jump's end, we need to move the end forward to cur jump's max index i.e. max_reach
            # and we need add one step
            if i == end:
                end = max_reach
                steps += 1
                # if the end is greater than n-1, means we don't need more steps to reach the end index of nums
                if end >= n - 1:
                    break

        return steps