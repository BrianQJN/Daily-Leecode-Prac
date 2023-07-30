"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
"""
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights:
            return []
        
        # 2 2D bool matrix to mark the cells that can flow to the pacific and atlantic
        m, n = len(heights), len(heights[0])
        res = []
        can_reach_pacific = [[False for _ in range(n)] for _ in range(m)]
        can_reach_atlantic = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(row, col, can_reach):
            can_reach[row][col] = True

            # offset from up, down, left and right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for r, c in directions:
                new_row, new_col = row + r, col + c
                if 0 <= new_row < m and 0 <= new_col < n and not can_reach[new_row][new_col] and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, can_reach)

        # start from the boundary of pacific, mark the cells that can flow to the pacific
        for i in range(m):
            dfs(i, 0, can_reach_pacific)
        for j in range(n):
            dfs(0, j, can_reach_pacific)

        # start from the boundary of atlantic, mark the cells that can flow to the atlantic
        for i in range(m):
            dfs(i, n - 1, can_reach_atlantic)
        for j in range(n):
            dfs(m - 1, j, can_reach_atlantic)

        # find the cells that can flow to both atlantic and pacific
        for i in range(m):
            for j in range(n):
                if can_reach_pacific[i][j] and can_reach_atlantic[i][j]:
                    res.append([i, j])

        return res