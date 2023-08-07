"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        
        # initialize four boundaries
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # traverse top boundary, from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            # after traversing, contract top boundary to bottom boundary
            top += 1

            # traverse right boundary, from top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            # after traversing, contract right boundary to left boundary
            right -= 1

            # if there is a bottom, traverse bottom boundary, from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                # after traversing, contract bottom boundary to top boundary
                bottom -=1

            # if there is a left, traverse left boundary, from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                # after traversing, contract left boundary to right boundary
                left += 1

        return res