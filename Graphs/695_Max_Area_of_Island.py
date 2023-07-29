"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0

Example:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        area = 0

        def dfs(row, col):
            # check the boundary conditions
            ## if row or col is out of bounds or position is water, return 0
            if row < 0 or row >=m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            
            # mark cur position as viewed
            grid[row][col] = 0

            # recursively view up, down, left and right adjacent positions
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
        
        # traverse all 2D grid
        for row in range(m):
            for col in range(n):
                # when meet land('1') and it is not viewd, call dfs
                if grid[row][col] == 1:
                    area = max(area, dfs(row, col))

        return area