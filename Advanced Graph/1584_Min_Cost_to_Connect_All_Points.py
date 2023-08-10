"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
"""
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # calculate the manhattan distance between two points
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        n = len(points)
        edges = []

        # calculate the manhattan distance between each point
        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan_distance(points[i], points[j])
                edges.append((distance, i, j))

        # sorted the edges by the distance
        edges.sort()

        # initialize the Union Find
        parent = list(range(n))

        def find(point):
            if parent[point] != point:
                parent[point] = find(parent[point])
            return parent[point]

        # using Kruskal algorithm to build a minimum spanning tree
        min_cost = 0
        num_connected = 0

        for distance, u, v in edges:
            parent_u = find(u)
            parent_v = find(v)

            if parent_u != parent_v:
                parent[parent_u] = parent_v
                min_cost += distance
                num_connected += 1

            if num_connected == n - 1:
                break

        return min_cost
    