"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution(object):
    def zigzagConversion(self, s, numRows):
        rows = [""] * numRows
        
        if numRows == 1:
            return s
        else:
            period = 2 * numRows - 2
            for i, char in enumerate(s):
                x = i % period
                rows[min(x, period-x)] += char
            return "".join(rows)
        

