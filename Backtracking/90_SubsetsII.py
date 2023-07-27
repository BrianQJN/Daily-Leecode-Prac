"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def dfs(start, cur):
            res.append(cur[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
                return
            
        dfs(0, [])

        return res