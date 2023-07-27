"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def dfs(start, target, cur):
            # if the target is 0, means that the current combination sum is equal to target, so append the cur to res
            if target == 0:
                res.append(cur[:])
                return
            
            for i in range(start, len(candidates)):
                # if current number is greater than target, means that the following nums is greater than target, so break the loop
                if candidates[i] > target:
                    break
                
                # if the cur number is not the first one in the candidate, and adjacent candidates are the same, we skip the cur to avoid duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # append the cur num to the cur combination, and call the dfs function recursively to construct the next possible combination
                cur.append(candidates[i])
                dfs(i + 1, target - candidates[i], cur)

                # backtracking to pop the num just appended to try other options
                cur.pop()

        dfs(0, target, [])

        return res