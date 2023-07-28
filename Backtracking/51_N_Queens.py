"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively

Example:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        def is_valid(board, row, col):
            # check if there is other Queens in cur column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                
            # check if there are other Queens in the top-left to bottom-right diagonal
            i, j = row - 1, col -1 
            while i >=0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j - 1
            # check if there are other Queens in the top-right to bottom-left diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i, j = i - 1, j + 1
            
            return True
        
        def backtrack(row):
            # if we have tried all the rows, we would get a valid result
            if row == n:
                res.append(board[:])
                return
            
            for col in range(n):
                # check if cur position is valid to put a Queen
                if is_valid(board, row, col):
                    # put the Queen
                    board[row][col] = 'Q'
                    # try put the Queen in next row
                    backtrack(row + 1)
                    # backtrack, remove the Queen we have set earlier
                    board[row][col] = '.'
        
        backtrack(0)

        return res