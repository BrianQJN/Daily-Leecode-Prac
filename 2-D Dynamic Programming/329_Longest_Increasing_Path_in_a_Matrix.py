"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9]
"""
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # initialize the dp array to record the longest path length from each cell
        dp = [[0] * cols for _ in range(rows)]

        # define the dfs function
        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]
            
            max_path = 1
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # if the value of next cell is greater than the cur cell, continue the dfs
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_path = max(max_path, 1 + dfs(new_row, new_col))

            dp[row][col] = max_path

            return max_path
        
        # apply dfs to each cell
        max_path_length = 0
        for i in range(rows):
            for j in range(cols):
                max_path_length = max(max_path_length, dfs(i, j))

        return max_path_length