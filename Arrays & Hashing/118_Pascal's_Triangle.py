"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # initialize the result list
        res = []

        # generate list for each row
        for i in range(numRows):
            # initialize the cur row, and set the default value
            cur_row = [0] * (i + 1)
            cur_row[0], cur_row[i] = 1, 1

            for j in range(1, i):
                cur_row[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(cur_row)

        return res