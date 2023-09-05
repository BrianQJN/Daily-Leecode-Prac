"""
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.

Example:
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
"""
class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        # initialize a hashtable to record the times a edge appeared
        edge_count = {}

        # traverse each row to count the edge appearance
        for row in wall:
            edge = 0
            # we need the edge except the right border
            for i in range(len(row)-1):
                edge += row[i]
                edge_count[edge] = edge_count.get(edge, 0) + 1

        max_edge_count = 0
        for edge in edge_count.values():
            max_edge_count = max(max_edge_count, edge)

        return len(wall) - max_edge_count