"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(cur, remaining):
            if not remaining:
                res.append(cur)
                return
            
            for i in range(len(remaining)):
                next_num = remaining[i]
                dfs(cur + [next_num], remaining[0:i] + remaining[i + 1:])

        dfs([], nums)

        return res