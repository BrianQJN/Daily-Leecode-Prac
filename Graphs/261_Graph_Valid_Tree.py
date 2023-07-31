"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # check whether the number of edges can construct a tree
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]

        # define the find function to find the parent node
        def find(node):
            if parent[node] == node:
                return node
            parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            parent[root_a] = root_b
            return True
        
        for edge in edges:
            # check whether there is a cycle during unioning
            a, b = edge[0], edge[1]
            if not union(a, b):
                return False
            
        return len(edges) == n - 1