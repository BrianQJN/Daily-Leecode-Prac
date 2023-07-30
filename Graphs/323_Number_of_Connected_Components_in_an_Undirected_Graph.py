"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
"""
from collections import Counter


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = [i for i in range(n)]

        def find(node):
            # find the parent node of cur node
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            # combine the two nodes
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
        
        for edge in edges:
            a, b = edge[0], edge[1]
            union(a, b)

        # count the number of root node in union find, if the parent[i] == i, means it is a root node
        count = sum(1 for i in range(n) if parent[i] == i)
        return count