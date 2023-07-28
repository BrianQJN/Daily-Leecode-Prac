"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            """
            i is the index of the row in board, j is the index of the column, k is the index of the char of the target word
            """
            # boundary condition
            # if cur position is out of board, or cur char is not equal to cur word char, return false
            if i < 0 or i > len(board) or j < 0 or j > len(board[0]) or board[i][j] != word[k]:
                return False
            
            # if we have found the full path, return true
            if k == len(word) - 1:
                return True
            
            # mark cur position as viewed
            tmp, board[i][j] = board[i][j], '/'

            # search the adjacent postion from up, down, left and right
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)

            # mark cur position as normal
            board[i][j] = tmp

            return res
        
        # traverse the board, looking for the position fix the first char in target word
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    # if we can find the full path, return true
                    if dfs(i, j, 0):
                        return True
                    
        return False