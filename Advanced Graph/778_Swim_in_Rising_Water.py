"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).

Example:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
"""
import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(-1,0),(1,0),(0,-1),(0,1)] # up, down, left, right
        visited = set()

        # using heaq to store the node we need to search
        heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))

        while heap:
            elevation, x, y = heapq.heappop(heap)

            # if we reached the end, return the elevation as result
            if x == n - 1 and y == n - 1:
                return elevation
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    new_elevation = max(elevation, grid[new_x][new_y])
                    heapq.heappush(heap, (new_elevation, new_x, new_y))
        
        # if no elevation returned, means can't reach the end, return -1
        return -1
            
