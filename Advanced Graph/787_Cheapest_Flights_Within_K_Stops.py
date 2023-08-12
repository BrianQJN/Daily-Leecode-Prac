"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""
import heapq
from collections import defaultdict


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # initialize a array costs to record the cost from srt to each city
        costs = [float('inf')] * n
        costs[src] = 0 # since from src to str needs 0 cost

        # we can only stop k+1 times after we departure from src
        for _ in range(k+1):
            new_costs = list(costs)
            for from_i, to_i, price in flights:
                new_costs[to_i] = min(new_costs[to_i], costs[from_i] + price)
            costs = new_costs

        return costs[dst] if costs[dst] != float('inf') else -1