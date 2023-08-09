"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
"""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticket_map = {}
        res = []

        for ticket in tickets:
            if ticket[0] not in ticket_map:
                ticket_map[ticket[0]] = []
            ticket_map[ticket[0]].append(ticket[1])

        for key in ticket_map:
            ticket_map[key].sort()

        def dfs(city):
            while ticket_map.get(city):
                next_city = ticket_map[city].pop(0)
                dfs(next_city)
            res.insert(0, city)

        dfs("JFK")

        return res
