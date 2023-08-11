"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # initialize the graph to record the start-point as key, end-point and time as value
        # initialize the dist to record the distance from node k to each node, default infinity means unreachable
        graph = {i: [] for i in range(1, n + 1)}
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0 # since node k to node k, the distance is zero

        # fill the graph using times
        for ui, vi, wi in times:
            graph[ui].append((vi, wi))

        print(graph)

        # create a min heap with (distance, node) pairs
        min_heap = [(0, k)]

        while min_heap:
            cur_dist, node = heapq.heappop(min_heap)

            # skip if the cur distance is greater than previous distance
            if cur_dist > dist[node]:
                continue

            # iterate over neighbors of the current node
            for neighbor, time in graph[node]:
                # update the distance if a shorter path is found
                if cur_dist + time < dist[neighbor]:
                    dist[neighbor] = cur_dist + time
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        
        # find the maximum time taken to receive the signal
        print(dist)
        max_time = max(dist.values())

        # if any node is unreachable, return -1, else max_time
        return max_time if max_time != float('inf') else -1


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
Solution.networkDelayTime(Solution, times, n, k)