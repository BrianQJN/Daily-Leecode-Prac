"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
"""
from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return None
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # find all gates and add them to queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))

        # offset from up, down, left and right directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            # start BFS from the current gate
            cur_row, cur_col = queue.popleft()

            for r, c in directions:
                new_row, new_col = cur_row + r, cur_col + c
                # boundary conditions, check if the new position is within the grid and is an empty room
                if 0 <= new_row < m and 0 <= new_col < n and rooms[new_row][new_col] == 2147483647:
                    # Update the distance to the gate and add the new position to the queue
                    rooms[new_row][new_col] = rooms[cur_row][cur_col] + 1
                    queue.append((new_row, new_col))