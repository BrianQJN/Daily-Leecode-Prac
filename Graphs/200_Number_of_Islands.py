"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        island_count = 0

        def dfs(row, col):
            # check the boundary conditions
            # if row or col out of bounds or position is water('0'), return
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
                return 
            
            # mark cur position as viewed
            grid[row][col] = '0'

            # recursively view the up, down, left and right adjacent positions
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        # traverse all 2D grid
        for row in range(m):
            for col in range(n):
                # when meet land('1') and it is not viewed, call dfs here and add 1 to island count
                if grid[row][col] == '1':
                    island_count += 1
                    dfs(row, col)
        
        return island_count

