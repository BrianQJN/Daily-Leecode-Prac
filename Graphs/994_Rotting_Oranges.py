"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
"""
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        minutes = 0

        # traverse the grid, add the rotting oranges to the queue, and record the num of fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1
        
        # offset from the up, down, left and right directions
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # if there are still some fresh oranges and rotten oranges, we need to call BFS to find the newest rotten oranges
        while queue and fresh_oranges > 0:
            # each iteration(BFS), we just rot the fresh oranges adjacent to the newest rotten oranges in last iteration
            for _ in range(len(queue)):
                cur_row, cur_col = queue.popleft()

                for r, c in directions:
                    new_row, new_col = cur_row + r, cur_col + c

                    # if the new position is fresh oranges, we rot it and add the position to the queue
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        fresh_oranges -= 1
            
            # after each iteration, we add one in minutes
            if queue:
                minutes += 1
        
        # check if there is still some fresh oranges, if yes, return -1, else minutes
        if fresh_oranges > 0:
            return -1
        else:
            return minutes