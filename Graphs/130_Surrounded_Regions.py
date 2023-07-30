"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return []
        
        # visited is used to record the cells that were visited, onborder is used to mark the border 'O'
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
 

        def dfs(row, col):
            visited[row][col] = True

            # offset of up, down, left, right directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for r, c in directions:
                new_row, new_col = row + r, col + c
                if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col] and board[row][col] == 'O':
                    dfs(new_row, new_col)
        
        # start from the four corners of the board to call the dfs function, mark the 'O' in the border, and mark them as unfliptable
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)
        
        # traverse the board, if the cell is 'O' and not in the visited, flip it to the 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
