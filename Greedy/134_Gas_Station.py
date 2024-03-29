"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        # initialize net_gas to record the net gas if we fill gas in gas[i] and then go to station i+1
        # net_gas = [gas[i] - cost[i] for i in range(n)]

        # if net_gas is less than 0, means wherever we choose to start, we can't make a cycle travel, return -1
        # if sum(net_gas) < 0:
        #     return -1
        
        # initialize total_gas to record the total net gas, cur_gas to record cur net gas, start to record start index
        total_gas, cur_gas, start = 0, 0, 0

        # traverse the net_gas array
        for i in range(n):
            total_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]

            # if cur_gas is less than 0 means if we start from this point, we can't reach next station, so we need to move forward
            if cur_gas < 0:
                cur_gas = 0
                start = i + 1

        return start if total_gas >= 0 else -1